import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pharmaconekt_secret_key_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- MODELOS DE BANCO DE DADOS ---

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nome = db.Column(db.String(100), nullable=False)

class Loja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    pdv_sistema = db.Column(db.String(50), nullable=False)  # Mapeamento do PDV
    status_onboarding = db.Column(db.String(20), default='Em Integração') # Em Integração, Ativo, Churn
    sugestoes_aceitas = db.Column(db.Integer, default=0)
    alertas_vencimento = db.Column(db.Integer, default=0)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# --- ROTAS DE AUTENTICAÇÃO ---

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Usuario.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- ROTAS DO DASHBOARD & OPERAÇÕES ---

@app.route('/dashboard')
@login_required
def dashboard():
    # Métricas baseadas nos OKRs e KPIs do documento descritivo
    total_lojas = Loja.query.count()
    lojas_ativas = Loja.query.filter_by(status_onboarding='Ativo').count()
    mrr_atual = total_lojas * 199  # Plano básico individual R$ 199
    
    # Simulação da taxa de aceitação do algoritmo (KPI 4)
    lojas = Loja.query.all()
    total_sugestoes = sum(l.sugestoes_aceitas for l in lojas)
    taxa_aceitacao = 75.5 if total_lojas > 0 else 0.0 

    return render_template('dashboard.html', 
                           total_lojas=total_lojas, 
                           lojas_ativas=lojas_ativas, 
                           mrr_atual=mrr_atual,
                           taxa_aceitacao=taxa_aceitacao)

# --- CRUD DE LOJAS (REDE FARMACÊUTICA) ---

@app.route('/lojas')
@login_required
def listar_lojas():
    lojas = Loja.query.all()
    return render_template('lojas.html', lojas=lojas)

@app.route('/lojas/nova', methods=['GET', 'POST'])
@login_required
def nova_loja():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cnpj = request.form.get('cnpj')
        pdv_sistema = request.form.get('pdv_sistema')
        status_onboarding = request.form.get('status_onboarding')
        
        nova = Loja(
            nome=nome, 
            cnpj=cnpj, 
            pdv_sistema=pdv_sistema, 
            status_onboarding=status_onboarding,
            sugestoes_aceitas=3, # Mock inicial para simular ativação
            alertas_vencimento=1
        )
        try:
            db.session.add(nova)
            db.session.commit()
            flash('Loja integrada com sucesso à rede PharmaConekt!', 'success')
            return redirect(url_for('listar_lojas'))
        except:
            db.session.rollback()
            flash('Erro: CNPJ já cadastrado.', 'danger')
            
    return render_template('nova_loja.html')

@app.route('/lojas/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_loja(id):
    loja = Loja.query.get_or_404(id)
    if request.method == 'POST':
        loja.nome = request.form.get('nome')
        loja.cnpj = request.form.get('cnpj')
        loja.pdv_sistema = request.form.get('pdv_sistema')
        loja.status_onboarding = request.form.get('status_onboarding')
        
        try:
            db.session.commit()
            flash('Dados da loja atualizados!', 'success')
            return redirect(url_for('listar_lojas'))
        except:
            db.session.rollback()
            flash('Erro ao atualizar os dados.', 'danger')
            
    return render_template('editar_loja.html', loja=loja)

@app.route('/lojas/deletar/<int:id>')
@login_required
def deletar_loja(id):
    loja = Loja.query.get_or_404(id)
    db.session.delete(loja)
    db.session.commit()
    flash('Loja removida da plataforma.', 'warning')
    return redirect(url_for('listar_lojas'))

# --- INICIALIZADOR DO BANCO DE DADOS ---

def inicializar_banco():
    with app.app_context():
        db.create_all()
        # Cria usuário administrador padrão caso não exista
        if not Usuario.query.filter_by(username='admin').first():
            senha_hash = generate_password_hash('admin123')
            admin = Usuario(username='admin', password=senha_hash, nome='Administrador PharmaConekt')
            db.session.add(admin)
            
            # Carga inicial de Lojas de Teste (Exemplos de Belém)
            loja1 = Loja(nome="Farmácia Belém Centro", cnpj="12.345.678/0001-01", pdv_sistema="Linx Farma", status_onboarding="Ativo", sugestoes_aceitas=5, alertas_vencimento=3)
            loja2 = Loja(nome="Drogaria Marco Express", cnpj="98.765.432/0001-99", pdv_sistema="Trier Sistemas", status_onboarding="Em Integração", sugestoes_aceitas=1, alertas_vencimento=0)
            db.session.add_all([loja1, loja2])
            
            db.session.commit()


@app.route('/dono')
def vista_dono():
    return render_template('dono_dashboard.html')

@app.route('/farma')
def vista_farma():
    return render_template('farmaceutico_dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)
    