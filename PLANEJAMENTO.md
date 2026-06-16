# 📊 PharmaConekt - Plano de Gerência e Engenharia de Software

Este documento detalha o planejamento estratégico, o escopo do MVP e a modelagem arquitetural da plataforma SaaS **PharmaConekt**.

---

## 1. INTRODUÇÃO

O **PharmaConekt** centraliza e unifica os dados de estoque e vendas entre farmácias independentes, micro-redes, distribuidores e sistemas de PDV na região metropolitana de Belém. O objetivo principal é mitigar os prejuízos causados por ilhas de informação isoladas, reduzindo rupturas e perdas por vencimento em até 40%.

* **Visão do Produto:** "Para farmácias independentes e micro-redes que sofrem com a desintegração de estoques, o PharmaConekt é um ecossistema SaaS que conecta PDVs e distribuidores, eliminando ilhas de informação e reduzindo perdas em até 40%."
* **Missão do MVP:** Entregar um barramento funcional em Python Flask com persistência SQLite capaz de gerenciar o onboarding e as métricas táticas de faturamento de forma ágil e centralizada.

---

## 2. ESTRUTURA ANALÍTICA DO PROJETO (EAP)

A decomposição hierárquica do trabalho para a construção completa do ecossistema:

```mermaid
graph TD
    A[PharmaConekt MVP] --> B[1. Discovery & Design]
    A --> C[2. Desenvolvimento]
    A --> D[3. Testes & QA]
    A --> E[4. Lançamento]

    B --> B1[1.1 Pesquisa com Farmácias]
    B --> B2[1.2 Backlog & Requisitos]
    B --> B3[1.3 Protótipos de Interface]

    C --> C1[2.1 Banco de Dados SQLite]
    C --> C2[2.2 Rotas e CRUD Flask]
    C --> C3[2.3 Painel de Métrica/KPI]

    D --> D1[3.1 Testes Unitários]
    D --> D2[3.2 Homologação com Pilotos]
    E --> E1[4.1 Deploy em Nuvem Cloud]
    E --> E2[4.2 Treinamento de Usuários]
```



## 3. CRONOGRAMA MACRO (GRÁFICO DE GANTT)

O cronograma de execução está planejado para uma janela de 5 meses (20 semanas):

```mermaid
gantt
    title Cronograma de Execução (5 Meses)
    dateFormat  YYYY-MM-DD
    axisFormat %m/%Y

    section Discovery 
    Pesquisa e Requisitos       :active, p1, 2026-03-01, 2026-03-15
    Backlog e Prototipação      : p2, 2026-03-15, 2026-03-31

    section Desenvolvimento
    Banco de Dados e Models     : p3, 2026-04-01, 2026-04-15
    Rotas, Auth e CRUD Flask    : p4, 2026-04-15, 2026-05-31
    Dashboard e KPIs            : p5, 2026-05-15, 2026-05-31

    section Testes & QA
    Testes de Integração        : p6, 2026-06-01, 2026-06-20
    Homologação com Pilotos     : p7, 2026-06-20, 2026-06-30

    section Lançamento
    Deploy em Produção          : p8, 2026-07-01, 2026-07-15
    Treinamento e Campanha      : p9, 2026-07-15, 2026-07-31
```

##4. DIAGRAMA DE FASES DO PROJETO

Ciclo de vida do projeto orientado por portões de decisão e marcos técnicos:
```mermaid
stateDiagram-v2
    [*] --> Discovery : Início do Projeto
    Discovery --> Desenvolvimento : Marco 1: Protótipo Aprovado
    Desenvolvimento --> Testes : Marco 2: Backend & CRUD Concluído
    Testes --> Lançamento : Marco 3: Homologação / UAT OK
    Lançamento --> [*] : Marco 4: Sistema em Produção
```

## 5. DIAGRAMA DE CASOS DE USO

Interações de atores externos e usuários com as funcionalidades previstas no escopo do MVP:

```mermaid
graph LR
    admin[Administrador Master] --- uc1(Fazer Login)
    admin --- uc2(Cadastrar Loja)
    admin --- uc3(Listar Lojas)

    dono[Dono de Farmácia] --- uc1
    dono --- uc4(Ver Dashboard de KPIs)

    cs[Operador de Onboarding] --- uc1
    cs --- uc5(Consultar Integração)
    cs --- uc6(Atualizar Status da Loja)

    pdv[Sistema de PDV Externo] --- uc7(Importar Dados de Vendas)

   ```

## 6. DIAGRAMA DE CLASSES

Estrutura das tabelas de dados gerenciadas pelas models do Flask:
```mermaid
classDiagram
    class Usuario {
        +int id
        +String nome
        +String username
        +String password_hash
        +fazer_login()
    }
    class Loja {
        +int id
        +String nome
        +String cnpj
        +String pdv_sistema
        +String status_onboarding
        +int sugestoes_aceitas
        +int alertas_vencimento
        +cadastrar()
        +editar()
        +excluir()
    }

    Usuario "1" --> "0..*" Loja : Gerencia/Monitora
```

## 7. COMPOSIÇÃO DA EQUIPE (SQUADS FUNCIONAIS)
Nos primeiros 12 meses, a empresa adota um modelo de squads funcionais enxutos, com hierarquia plana, comunicação direta e regime de trabalho remoto-assíncrono. O escritório físico compartilhado localiza-se nos bairros do Marco ou Batista Campos, em Belém.A equipe é composta por 9 integrantes, divididos da seguinte forma:

```mermaid
graph TD
    CEO["CEO / Founder<br>Visão, Captação e Parcerias"] --> DevSquad["Dev Squad<br>2 Devs Full-Stack"]
    CEO --> DataSquad["Data Squad<br>1 Engenheiro de Dados"]
    COO["COO / Founder<br>Operações e Customer Success"] --> OnboardSquad["Onboarding Squad<br>1 Analista de Implantação"]
    COO --> CS["Customer Success<br>1 Analista Farmacêutico"]
    CTO["CTO / Founder<br>Produto, Arquitetura e Segurança"] --> DevSquad
    Vendas["Vendas<br>1 SDR"] --- CEO

```

Liderança Executiva:

    CEO / Founder: Responsável pela visão de negócio, captação de recursos e parcerias com distribuidoras regionais e o Sindicato dos Farmacêuticos do Pará (Sinfarpa).
    CTO / Founder: Lidera o produto, segurança e garante latência mínima de 5 segundos para a união instantânea de dados.

    COO / Founder: Gerencia as operações, focado no onboarding e retenção.

Estrutura dos Squads:
    Dev Squad (2 Devs Full-Stack): Um focado em backend/integrações e outro em frontend/dashboards.

    Data Squad (1 Engenheiro de Dados): Responsável pelos fluxos de dados e algoritmos de previsão de demanda (média móvel e ajuste sazonal).

    Onboarding Squad (1 Analista de Implantação): Realiza a carga inicial de dados (Top 200 SKUs), configuração e treinamento remoto de 30 minutos.

    Customer Success (1 Analista Farmacêutico): Fornece suporte especializado em regras da Anvisa, controle de lotes e receitas.

    Vendas (1 SDR): Prospecção activa via WhatsApp e visitas físicas em Belém.
```
```
## 8. MODELO DE PRECIFICAÇÃO E RECEITA

O modelo comercial foi estruturado especificamente para o formato SaaS (Software as a Service) B2B, focado na recorrência.
8.1. Estrutura de Receita (Assinatura Mensal)

    Plano Loja Individual: R$ 199,00 por mês.

    Plano Rede (Até 5 lojas integradas): R$ 399,00 por mês.

8.2. Investimento do MVP (Preço Fixo)

Para a construção, validação e estabilização do barramento Flask com banco SQLite que você possui no código, o valor comercial fechado do projeto está estipulado em R$ 120.000,00, com pagamentos atrelados aos seguintes marcos técnicos:

    30% na Entrada: Homologação dos protótipos de tela.

    30% na Entrega Intermediária: Banco de dados SQLite estruturado e rotas de CRUD operacionais.

    40% no Encerramento: Liberação do Dashboard com métricas e homologação concluída.

## 9. METODOLOGIA OKR E KPIs SEMANAIS

Alinhado aos objetivos estratégicos do negócio, a gestão monitora o desempenho através de metas anuais e indicadores semanais.
9.1. OKR Anual (Foco em Validação e Tração)

    Objetivo Estratégico: Validar o modelo de negócio e atingir tração inicial no mercado paraense de farmácias independentes, demonstrando prontidão para uma rodada de captação seed.

        KR1 (Aquisição): Fechar 30 farmácias pagantes até o mês 12, gerando um MRR (Faturamento Recorrente Mensal) de R$ 5.970,00.

        KR2 (Eficiência): Reduzir o tempo de onboarding para menos de 3 dias úteis (mediana) até o mês 9.

        KR3 (Satisfação): Alcançar Net Promoter Score (NPS) >= 50 entre os clientes ativos no mês 12.

9.2. KPIs Semanais (Métricas Táticas Operacionais)

Diferente dos KRs (que medem resultados de longo prazo), os KPIs são acompanhados semanalmente para ajustes rápidos de rota:

    Farmácias em Demonstração: Meta de >= 3 apresentações realizadas por semana (Dono: SDR).

    Tempo de Ativação: Meta de mediana < 36 hours para o cliente completar as primeiras configurações (Dono: Onboarding Squad).

    Churn Semanal: Meta de < 2% de cancelamentos na semana (Dono: Customer Success).

    Taxa de Aceitação de Sugestões: Meta de > 60% das sugestões automáticas aplicadas pelo cliente (Dono: Data Squad).

    Crescimento Líquido de Clientes Ativos: Ganho de 1 a 2 novas farmácias integradas por semana (Dono: CEO).

## 10. PROCESSO CRÍTICO E CRITÉRIOS DE ACEITE (HOMOLOGAÇÃO)
10.1. O Fluxo de Onboarding (5 a 7 dias úteis)

O onboarding é o processo crítico porque dita a retenção do cliente no ecossistema SaaS. O fluxo funciona assim:

    Prospecção & Demo: SDR qualifica a farmácia e os fundadores realizam a disposição.

    Assinatura & Coleta: Coleta da versão do PDV, lista de distribuidores e catálogo dos Top 200 SKUs.

    Configuração Técnico (Em até 48h): Importação de lotes, estoques e datas de validade pelo Onboarding Squad.

    Treinamento & Ativação: Treinamento remoto de 30 minutos. O cliente é considerado "Ativado" quando aceita pelo menos 3 sugestões de compra consecutivas e resolve seu primeiro alerta de vencimento em tela.

10.2. Critérios de Aceite para Entrega do Software

O projeto de software será dado como concluído e aceito quando cumprir os seguintes requisitos práticos verificáveis no código:

    Ciclo de Vida das Lojas (CRUD): O administrador consegue cadastrar novas lojas, listar, editar dados de integração e atualizar o status sem falhas ou exceções no banco database.db (SQLite).

    Cálculo Automatizado de KPIs: O painel (Dashboard) exibe de forma clara e dinâmica as regras de MRR baseadas na quantidade de lojas ativas.

    Teste de Validação de Usuário (UAT): Execução com sucesso onde o usuário simula o fluxo completo (Login -> Visualização das Lojas -> Edição de Status de Onboarding) sem necessidade de suporte técnico do desenvolvedor.

