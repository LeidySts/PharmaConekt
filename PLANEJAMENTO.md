# 📊 PharmaConekt - Plano de Gerência e Engenharia de Software

[cite_start]Este documento detalha o planejamento estratégico, o escopo do MVP e a modelagem arquitetural da plataforma SaaS **PharmaConekt**[cite: 115, 116].

---

## 1. INTRODUÇÃO

[cite_start]O **PharmaConekt** centraliza e unifica os dados de estoque e vendas entre farmácias independentes, micro-redes, distribuidores e sistemas de PDV na região metropolitana de Belém[cite: 115, 116, 118]. [cite_start]O objetivo principal é mitigar os prejuízos causados por ilhas de informação isoladas, reduzindo rupturas e perdas por vencimento em até 40%[cite: 116, 117, 119].

* [cite_start]**Visão do Produto:** "Para farmácias independentes e micro-redes que sofrem com a desintegração de estoques, o PharmaConekt é um ecossistema SaaS que conecta PDVs e distribuidores, eliminando ilhas de informação e reduzindo perdas em até 40%." [cite: 116, 119]
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

    gantt
    title Cronograma de Execução (5 Meses)
    dateFormat  YYYY-MM-DD
    axisFormat %m/%Y

    section Discovery & Design
    Pesquisa e Requisitos       :active, p1, 2026-03-01, 2026-03-15
    Backlog e Prototipação      : p2, 2026-03-15, 2026-03-31

    section Desenvolvimento Core
    Banco de Dados e Models     : p3, 2026-04-01, 2026-04-15
    Rotas, Autenticação e CRUD  : p4, 2026-04-15, 2026-05-31
    Dashboard e KPIs            : p5, 2026-05-15, 2026-05-31

    section Testes & QA
    Testes de Integração        : p6, 2026-06-01, 2026-06-20
    Homologação com Pilotos     : p7, 2026-06-20, 2026-06-30

    section Lançamento
    Deploy em Produção          : p8, 2026-07-01, 2026-07-15
    Treinamento e Campanha      : p9, 2026-07-15, 2026-07-31

    stateDiagram-v2
    [*] --> Discovery : Início do Projeto
    Discovery --> Desenvolvimento : Marco 1: Protótipo Aprovado
    Desenvolvimento --> Testes : Marco 2: Backend & CRUD Concluído
    Testes --> Lançamento : Marco 3: Homologação / UAT OK
    Lançamento --> [*] : Marco 4: Sistema em Produção

    leftToRightDirection
actor "Administrador Master" as admin
actor "Dono de Farmácia" as dono
actor "Operador de Onboarding" as cs
actor "Sistema de PDV Externo" as pdv

rectangle "Plataforma PharmaConekt (MVP)" {
    admin --> (Fazer Login)
    dono --> (Fazer Login)
    cs --> (Fazer Login)
    
    admin --> (Cadastrar Loja)
    admin --> (Listar Lojas)
    dono --> (Ver Dashboard de KPIs)
    
    cs --> (Consultar Integração)
    cs --> (Atualizar Status da Loja)
    
    pdv --> (Importar Dados de Vendas)
}

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
    ## 7. COMPOSIÇÃO DA EQUIPE (SQUADS FUNCIONAIS)

Nos primeiros 12 meses, a empresa adota um modelo de squads funcionais enxutos, com hierarquia plana, comunicação direta e regime de trabalho remoto-assíncrono. O escritório físico compartilhado localiza-se nos bairros do Marco ou Batista Campos, em Belém. 

A equipe é composta por 9 integrantes, divididos da seguinte forma:

```mermaid
graph TD
    CEO[CEO / Founder<br>Visão, Captação e Parcerias] --> DevSquad
    CEO --> DataSquad
    COO[COO / Founder<br>Operações e Customer Success] --> OnboardSquad
    COO --> CS
    CTO[CTO / Founder<br>Produto, Arquitetura e Segurança] --> DevSquad
    
    subgraph Squads
        DevSquad[Dev Squad<br>2 Devs Full-Stack]
        DataSquad[Data Squad<br>1 Engenheiro de Dados]
        OnboardSquad[Onboarding Squad<br>1 Analista de Implantação]
        CS[Customer Success<br>1 Analista Farmacêutico]
    end
    
    Vendas[Vendas<br>1 SDR] --- CEO
    