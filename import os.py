import os

# 1. Cria a estrutura de pastas
pastas = ["templates", "static/css", "static/js"]
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)

# 2. Cria os arquivos vazios para você apenas colar o conteúdo
arquivos = [
    "app.py",
    "requirements.txt",
    "README.md",
    "static/css/style.css",
    "static/js/main.js",
    "templates/base.html",
    "templates/login.html",
    "templates/dashboard.html",
    "templates/lojas.html",
    "templates/nova_loja.html",
    "templates/editar_loja.html",
]

for arquivo in arquivos:
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("")  # Cria o arquivo limpo

print("🎯 Estrutura criada! Agora abra a pasta e preencha os arquivos.")
