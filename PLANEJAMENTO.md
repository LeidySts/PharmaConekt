# 📊 PharmaConekt - Plano de Gerência e Engenharia de Software

Este documento detalha o planejamento estratégico, o escopo do MVP e a modelagem arquitetural da plataforma SaaS **PharmaConekt**.

---

## 1. INTRODUÇÃO

O PharmaConekt evoluiu de um simples integrador de estoques para um ecossistema completo de gestão farmacêutica, transformando dados em decisões lucrativas para farmácias independentes e micro-redes na região metropolitana de Belém. O sistema unifica operações (PDV, estoque, caixas, entregas e multi lojas), gestão comercial (clientes, financeiro, vendas, comissões e insights) e estratégia (dashboard, fidelidade, alertas, relatórios e OneBot), eliminando ilhas de informação e capacitando o gestor a competir com as grandes redes. O objetivo principal é reduzir perdas por vencimento e ruptura em até 40%, enquanto aumenta o faturamento com inteligência de dados, sugestões contextualizadas de venda e otimização de preços baseada em análise de mercado.

Visão do Produto: "Para farmácias independentes e micro-redes que buscam crescer lucrativamente em um mercado competitivo, o PharmaConekt é um ecossistema SaaS que integra operações, finanças e estratégia, transformando dados em decisões lucrativas e reduzindo perdas em até 40%."

Missão do MVP: Entregar uma plataforma web funcional e intuitiva, com persistência de dados em nuvem, capaz de gerenciar o onboarding, as métricas táticas de faturamento, o programa de fidelidade, os insights de mercado e os alertas inteligentes de forma ágil, centralizada e com dados sincronizados em menos de 5 segundos.

---

## 2. ESTRUTURA ANALÍTICA DO PROJETO (EAP)

A decomposição hierárquica do trabalho para a construção completa do ecossistema:

```mermaid
graph TD
    A[🏥 PharmaConekt<br/>Ecossistema Completo] --> B[1. FUNDAÇÃO DO SISTEMA]
    A --> C[2. NÚCLEO OPERACIONAL]
    A --> D[3. ESTRATÉGIA & CRESCIMENTO]
    A --> E[4. COMERCIAL & CLIENTES]
    A --> F[5. FINANCEIRO]
    A --> G[6. INTEGRAÇÃO & SUPORTE]

    B --> B1[Planejamento]
    B --> B2[Arquitetura]
    B --> B3[Infraestrutura]
    B --> B4[Segurança]
    B --> B5[UI/UX Design]

    C --> C1[🛒 PDV]
    C --> C2[📦 Estoque]
    C --> C3[🏢 Multi Lojas]
    C --> C4[🖥️ Caixas]
    C --> C5[🛵 Entregas]
    C --> C6[🛒 Compras]

    D --> D1[📊 Dashboard]
    D --> D2[⭐ Fidelidade]
    D --> D3[📈 Insights]
    D --> D4[🔔 Alertas]

    E --> E1[👤 Clientes]
    E --> E2[👔 Funcionários]
    E --> E3[📈 Vendas]
    E --> E4[💰 Comissões]

    F --> F1[📋 Contas]
    F --> F2[💵 Fluxo de Caixa]
    F --> F3[📊 DRE]
    F --> F4[🏢 Fornecedores]
    F --> F5[📄 Exportação]

    G --> G1[🤖 OneBot]
    G --> G2[🔗 Integrações]
    G --> G3[⚙️ Configurações]
    G --> G4[💬 Suporte]
    G --> G5[📋 Relatórios]

    classDef raiz fill:#003366,color:#fff,stroke:#002244,stroke-width:2px,font-size:16px
    classDef nivel1 fill:#1a4f7a,color:#fff,stroke:#002244,stroke-width:2px
    classDef nivel2 fill:#e8edf4,color:#1a2a3a,stroke:#d5dde8,stroke-width:1px

    class A raiz
    class B,C,D,E,F,G nivel1
    class B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,C6,D1,D2,D3,D4,E1,E2,E3,E4,F1,F2,F3,F4,F5,G1,G2,G3,G4,G5 nivel2
```

## 2.1 VERSÃO INTERATIVA POR MÓDULO
```mermaid
graph LR
    subgraph "1. FUNDAÇÃO"
        B1[Planejamento] --> B2[Arquitetura]
        B2 --> B3[Infraestrutura]
        B3 --> B4[Segurança]
        B4 --> B5[UI/UX Design]
    end

    subgraph "2. NÚCLEO OPERACIONAL"
        C1[🛒 PDV] --> C2[📦 Estoque]
        C2 --> C3[🏢 Multi Lojas]
        C3 --> C4[🖥️ Caixas]
        C4 --> C5[🛵 Entregas]
        C5 --> C6[🛒 Compras]
    end

    subgraph "3. ESTRATÉGIA"
        D1[📊 Dashboard] --> D2[⭐ Fidelidade]
        D2 --> D3[📈 Insights]
        D3 --> D4[🔔 Alertas]
    end

    subgraph "4. COMERCIAL"
        E1[👤 Clientes] --> E2[👔 Funcionários]
        E2 --> E3[📈 Vendas]
        E3 --> E4[💰 Comissões]
    end

    subgraph "5. FINANCEIRO"
        F1[📋 Contas] --> F2[💵 Fluxo de Caixa]
        F2 --> F3[📊 DRE]
        F3 --> F4[🏢 Fornecedores]
        F4 --> F5[📄 Exportação]
    end

    subgraph "6. INTEGRAÇÃO"
        G1[🤖 OneBot] --> G2[🔗 Integrações]
        G2 --> G3[⚙️ Configurações]
        G3 --> G4[💬 Suporte]
        G4 --> G5[📋 Relatórios]
    end

    C2 -.-> D1
    C1 -.-> E1
    C6 -.-> F1
    E1 -.-> D2
    F3 -.-> D1
    G1 -.-> E1

    classDef subg fill:#f0f4f9,color:#1a2a3a,stroke:#d5dde8,stroke-width:2px
    classDef modulo fill:#e8edf4,color:#1a2a3a,stroke:#d5dde8,stroke-width:1px
    
    class B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,C6,D1,D2,D3,D4,E1,E2,E3,E4,F1,F2,F3,F4,F5,G1,G2,G3,G4,G5 modulo
```

## 2.2 MATRIZ DE DEPENDÊNCIAS
```mermaid
graph TD
    subgraph "DEPENDÊNCIAS ENTRE MÓDULOS"
        A[1. FUNDAÇÃO] --> B[2. NÚCLEO OPERACIONAL]
        A --> C[3. ESTRATÉGIA]
        A --> D[4. COMERCIAL]
        A --> E[5. FINANCEIRO]
        A --> F[6. INTEGRAÇÃO]

        B --> C
        B --> D
        B --> E
        B --> F

        C --> D
        C --> E

        D --> E
        D --> F

        E --> F
    end

    classDef dep fill:#003366,color:#fff,stroke:#002244,stroke-width:2px
    class A,B,C,D,E,F dep
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

## 4. DIAGRAMA DE FASES DO PROJETO

Ciclo de vida do projeto orientado por portões de decisão e marcos técnicos:
```mermaid
stateDiagram-v2
    [*] --> Discovery : Início do Projeto
    Discovery --> Desenvolvimento : Marco 1: Protótipo Aprovado
    Desenvolvimento --> Testes : Marco 2: Backend & CRUD Concluído
    Testes --> Lançamento : Marco 3: Homologação / UAT OK
    Lançamento --> [*] : Marco 4: Sistema em Produção
```

## 5. DIAGRAMA DE CASO DE USOS 

Interações de atores externos e usuários com as funcionalidades previstas no escopo do MVP:

## 5.1 DIAGRAMA DETALHADO - DONO/ADMINISTRADOR

```mermaid
graph TD
    subgraph "DONO/ADMINISTRADOR - PERMISSÕES TOTAIS"
        A1[👑 Dono/Administrador]
        
        A1 --> PDV[PDV]
        A1 --> ESTOQUE[Estoque]
        A1 --> FIDELIDADE[Fidelidade]
        A1 --> FINANCEIRO[Financeiro]
        A1 --> INSIGHTS[Insights]
        A1 --> GESTAO[Gestão]
        A1 --> CONFIG[Configurações]
        A1 --> RELATORIOS[Relatórios]
        A1 --> ONEBOT[OneBot]

        PDV --> P1[Realizar Venda]
        PDV --> P2[Consultar Histórico]
        PDV --> P3[Gerenciar Caixas]

        ESTOQUE --> E1[Gerenciar Estoque]
        ESTOQUE --> E2[Cadastrar Produtos]
        ESTOQUE --> E3[Transferir Produtos]
        ESTOQUE --> E4[Receber XML]

        FIDELIDADE --> F1[Configurar Programa]
        FIDELIDADE --> F2[Ver Todos Clientes]
        FIDELIDADE --> F3[Ver Relatórios]

        FINANCEIRO --> FI1[Gerenciar Contas]
        FINANCEIRO --> FI2[Visualizar DRE]
        FINANCEIRO --> FI3[Visualizar Fluxo]
        FINANCEIRO --> FI4[Exportar Relatórios]

        INSIGHTS --> I1[Ver Dashboard]
        INSIGHTS --> I2[Ver Alertas]
        INSIGHTS --> I3[Analisar Mercado]

        GESTAO --> G1[Gerenciar Funcionários]
        GESTAO --> G2[Gerenciar Lojas]
        GESTAO --> G3[Gerenciar Clientes]
        GESTAO --> G4[Gerenciar Fornecedores]

        CONFIG --> C1[Configurar Sistema]
        CONFIG --> C2[Backup em Nuvem]
        CONFIG --> C3[Gerenciar Permissões]
        CONFIG --> C4[Integrações]

        RELATORIOS --> R1[Relatório Financeiro]
        RELATORIOS --> R2[Relatório Vendas]
        RELATORIOS --> R3[Relatório Estoque]
        RELATORIOS --> R4[Relatório Fidelidade]
        RELATORIOS --> R5[Relatório Gerencial]

        ONEBOT --> O1[Configurar OneBot]
        ONEBOT --> O2[Ver Atendimentos]
        ONEBOT --> O3[Ver Estatísticas]
    end

    classDef dono fill:#003366,color:#fff,stroke:#002244,stroke-width:2px,font-size:16px
    classDef modulo fill:#1a4f7a,color:#fff,stroke:#002244,stroke-width:1px
    classDef caso fill:#e8edf4,color:#1a2a3a,stroke:#d5dde8,stroke-width:1px

    class A1 dono
    class PDV,ESTOQUE,FIDELIDADE,FINANCEIRO,INSIGHTS,GESTAO,CONFIG,RELATORIOS,ONEBOT modulo
    class P1,P2,P3,E1,E2,E3,E4,F1,F2,F3,FI1,FI2,FI3,FI4,I1,I2,I3,G1,G2,G3,G4,C1,C2,C3,C4,R1,R2,R3,R4,R5,O1,O2,O3 caso

   ```

## 5.2 DIAGRAMA DETALHADO - VENDEDOR

```mermaid
graph TD
    subgraph "VENDEDOR - PERMISSÕES OPERACIONAIS"
        A3[🛒 Vendedor]
        
        A3 --> PDV[PDV]
        A3 --> ESTOQUE[Estoque]
        A3 --> FIDELIDADE[Fidelidade]
        A3 --> CLIENTES[Clientes]

        PDV --> P1[Realizar Venda]
        PDV --> P2[Buscar Produto]
        PDV --> P3[Adicionar ao Carrinho]
        PDV --> P4[Finalizar Compra]
        PDV --> P5[Emitir Comprovante]
        PDV --> P6[Consultar Bula]
        PDV --> P7[Aplicar Desconto]
        PDV --> P8[Sugerir Produtos]
        PDV --> P9[Registrar Cliente]

        ESTOQUE --> E1[Consultar Estoque]
        ESTOQUE --> E2[Ver Alertas]

        FIDELIDADE --> F1[Ver Pontos Cliente]
        FIDELIDADE --> F2[Resgatar Pontos]

        CLIENTES --> C1[Consultar Clientes]
        CLIENTES --> C2[Cadastrar Cliente]
    end

    classDef vendedor fill:#f5a623,color:#333,stroke:#e69500,stroke-width:2px,font-size:16px
    classDef modulo fill:#f9a825,color:#333,stroke:#e69500,stroke-width:1px
    classDef caso fill:#e8edf4,color:#1a2a3a,stroke:#d5dde8,stroke-width:1px

    class A3 vendedor
    class PDV,ESTOQUE,FIDELIDADE,CLIENTES modulo
    class P1,P2,P3,P4,P5,P6,P7,P8,P9,E1,E2,F1,F2,C1,C2 caso


   ```

## 5.3 DIAGRAMA DETALHADO - CLIENTE

```mermaid
graph TD
    subgraph "CLIENTE - INTERAÇÕES PÚBLICAS"
        A5[👤 Cliente]
        
        A5 --> PDV[PDV]
        A5 --> FIDELIDADE[Fidelidade]
        A5 --> ONEBOT[OneBot]

        PDV --> P1[Realizar Compra]
        PDV --> P2[Emitir Comprovante]
        PDV --> P3[Consultar Bula]

        FIDELIDADE --> F1[Ver Pontos]
        FIDELIDADE --> F2[Resgatar Pontos]
        FIDELIDADE --> F3[Ver Nível]

        ONEBOT --> O1[Fazer Perguntas]
        ONEBOT --> O2[Agendar Serviço]
        ONEBOT --> O3[Programar Lembrete]
    end

    classDef cliente fill:#00838f,color:#fff,stroke:#006064,stroke-width:2px,font-size:16px
    classDef modulo fill:#00acc1,color:#fff,stroke:#00838f,stroke-width:1px
    classDef caso fill:#e8edf4,color:#1a2a3a,stroke:#d5dde8,stroke-width:1px

    class A5 cliente
    class PDV,FIDELIDADE,ONEBOT modulo
    class P1,P2,P3,F1,F2,F3,O1,O2,O3 caso

   ```

## 6. DIAGRAMA DE CLASSES

Estrutura das tabelas de dados gerenciadas pelas models do Flask:

## 6.1 MÓDULO DE SEGURANÇA E AUTENTICAÇÃO
```mermaid
classDiagram
    class Usuario {
        -int id
        -String nome
        -String email
        -String password_hash
        -String perfil
        -DateTime created_at
        -DateTime updated_at
        +login() bool
        +logout() void
        +tem_permissao(String modulo) bool
    }

    class Perfil {
        -int id
        -String nome
        -String descricao
        -List~String~ permissoes
        +add_permissao(String modulo) void
        +remove_permissao(String modulo) void
    }

    class Sessao {
        -int id
        -int usuario_id
        -String token
        -DateTime expiracao
        +validar() bool
        +renovar() void
    }

    Usuario "1" --> "1" Perfil : Possui
    Usuario "1" --> "0..*" Sessao : Possui
```

## 6.2 MÓDULO OPERACIONAL (PDV + ESTOQUE)
```mermaid
classDiagram
    class PDV {
        -int id
        -int loja_id
        -int caixa_id
        -String status
        -DateTime abertura
        -DateTime fechamento
        +abrir() bool
        +fechar() bool
        +registrar_venda(Venda venda) bool
        +consultar() Dict
    }

    class Carrinho {
        -int id
        -int pdv_id
        -int cliente_id
        -List~ItemVenda~ itens
        -float desconto
        -float total
        +adicionar_item(Produto produto, int quantidade) void
        +remover_item(int item_id) void
        +aplicar_desconto(float percentual) void
        +finalizar() Venda
    }

    class Estoque {
        -int id
        -int produto_id
        -int loja_id
        -int quantidade
        -int quantidade_minima
        +consultar() int
        +ajustar(int nova_quantidade) void
        +verificar_critico() bool
        +transferir(int quantidade, Loja destino) bool
    }

    class MovimentacaoEstoque {
        -int id
        -int produto_id
        -int loja_id
        -int quantidade
        -String tipo
        -String motivo
        -DateTime data
        +registrar() void
    }

    PDV "1" --> "0..*" Carrinho : Possui
    Carrinho "1" --> "0..*" ItemVenda : Contém
    Estoque "1" --> "0..*" MovimentacaoEstoque : Registra
    Produto "1" --> "0..*" Estoque : Possui
```

## 6.3 MÓDULO DE FIDELIDADE
```mermaid
classDiagram
    class Fidelidade {
        -int id
        -int cliente_id
        -int pontos
        -String nivel
        -DateTime data_atualizacao
        +acumular_pontos(int pontos) void
        +resgatar_pontos(int pontos, String produto) bool
        +calcular_nivel() String
        +get_pontos_para_proximo_nivel() int
    }

    class NivelFidelidade {
        -String nome
        -int pontos_minimo
        -int pontos_maximo
        -float desconto
        -String beneficios
        +get_nivel_by_pontos(int pontos) String
        +get_desconto(String nivel) float
    }

    class HistoricoPontos {
        -int id
        -int fidelidade_id
        -String descricao
        -int pontos
        -String tipo
        -DateTime data
        +registrar() void
    }

    class Resgate {
        -int id
        -int fidelidade_id
        -String produto
        -int pontos_gastos
        -DateTime data
        +confirmar() bool
        +cancelar() bool
    }

    Fidelidade "1" --> "1" NivelFidelidade : Possui
    Fidelidade "1" --> "0..*" HistoricoPontos : Registra
    Fidelidade "1" --> "0..*" Resgate : Realiza
```

## 6.4 MÓDULO FINANCEIRO
```mermaid
classDiagram
    class MovimentacaoFinanceira {
        -int id
        -String tipo
        -String descricao
        -String categoria
        -float valor
        -Date data
        -Date vencimento
        -String fornecedor
        -String forma_pagamento
        -String status
        -String observacoes
        +registrar() bool
        +pagar() bool
        +editar() bool
        +excluir() bool
    }

    class CategoriaFinanceira {
        -int id
        -String nome
        -String tipo
        -String cor
        +get_by_tipo(String tipo) List~CategoriaFinanceira~
    }

    class FluxoCaixa {
        -int id
        -Date periodo_inicio
        -Date periodo_fim
        -float total_entradas
        -float total_saidas
        -float saldo
        +calcular() Dict
        +gerar_relatorio() String
    }

    class DRE {
        -int id
        -Date periodo
        -float receitas_totais
        -float custos_totais
        -float despesas_operacionais
        -float impostos
        -float lucro_liquido
        -float margem_lucro
        +calcular() Dict
        +gerar_relatorio() String
    }

    class Fornecedor {
        -int id
        -String nome
        -String cnpj
        -String telefone
        -float total_compras
        -String status
        +cadastrar() bool
        +editar() bool
        +excluir() bool
    }

    MovimentacaoFinanceira "1" --> "1" CategoriaFinanceira : Pertence
    MovimentacaoFinanceira "1" --> "0..1" Fornecedor : Vinculado
    FluxoCaixa "1" --> "0..*" MovimentacaoFinanceira : Agrupa
    DRE "1" --> "0..*" MovimentacaoFinanceira : Agrupa
```

## 6.5 MÓDULO DE INSIGHTS E DASHBOARD
```mermaid
classDiagram
    class Dashboard {
        -int id
        -int loja_id
        -float total_receitas
        -float total_vendas
        -int transacoes
        -float ticket_medio
        -int clientes_ativos
        -DateTime data
        +calcular_metricas() Dict
        +gerar_graficos() Dict
        +atualizar() void
    }

    class Insight {
        -int id
        -String tipo
        -String descricao
        -Dict dados
        -float preco_sugerido
        -float preco_mercado
        -DateTime data
        +analisar_precos() Dict
        +sugerir_preco() float
        +prever_vendas() Dict
    }

    class Alertas {
        -int id
        -String tipo
        -String mensagem
        -Date data_criacao
        -int produto_id
        -int loja_id
        -boolean visualizado
        +criar() bool
        +visualizar() void
        +get_alertas_ativos() List~Alertas~
    }

    class Relatorio {
        -int id
        -String titulo
        -String tipo
        -Dict dados
        -DateTime data_criacao
        +gerar() String
        +exportar(String formato) File
        +imprimir() void
    }

    Dashboard "1" --> "0..*" Insight : Gera
    Alertas "1" --> "0..1" Produto : Notifica
    Dashboard "1" --> "0..*" Relatorio : Cria
```

## 6.6 MÓDULO DE INTEGRAÇÃO (ONEBOT)
```mermaid
classDiagram
    class OneBot {
        -int id
        -String nome
        -String idioma
        -int tempo_resposta
        -String tema
        -String saudacao
        -DateTime created_at
        -DateTime updated_at
        +responder(String pergunta) String
        +agendar_servico(String servico) bool
        +programar_lembrete(String medicamento, String horario) bool
        +get_estatisticas() Dict
    }

    class ChatOneBot {
        -int id
        -String cliente
        -String mensagem
        -String resposta
        -DateTime data
        +salvar() void
        +get_historico(String cliente) List~ChatOneBot~
    }

    class PerguntaFrequente {
        -int id
        -String pergunta
        -String resposta
        -String categoria
        -int frequencia
        +cadastrar() bool
        +editar() bool
        +excluir() bool
    }

    class Lembrete {
        -int id
        -int onebot_id
        -String medicamento
        -String horario
        -boolean ativo
        -DateTime created_at
        +ativar() void
        +desativar() void
        +notificar() void
    }

    class Agendamento {
        -int id
        -int onebot_id
        -String servico
        -DateTime data
        -String cliente
        -String status
        +confirmar() bool
        +cancelar() bool
        +reagendar(DateTime nova_data) bool
    }

    OneBot "1" --> "0..*" ChatOneBot : Possui
    OneBot "1" --> "0..*" PerguntaFrequente : Utiliza
    OneBot "1" --> "0..*" Lembrete : Cria
    OneBot "1" --> "0..*" Agendamento : Gerencia
```

## 6.7 MÓDULO DE ENTREGAS
```mermaid
classDiagram
    class Entrega {
        -int id
        -int venda_id
        -String cliente
        -String telefone
        -String endereco
        -String produto
        -String entregador
        -float valor
        -String status
        -int prazo
        -String observacoes
        -DateTime data_criacao
        -DateTime data_entrega
        +atualizar_status(String novo_status) void
        +cancelar() bool
        +get_historico_status() List~StatusEntrega~
    }

    class StatusEntrega {
        -int id
        -int entrega_id
        -String status
        -DateTime data
        +registrar() void
    }

    class Entregador {
        -int id
        -String nome
        -String telefone
        -String veiculo
        -String placa
        -String status
        -List~Entrega~ entregas
        +atribuir_entrega(Entrega entrega) void
        +finalizar_entrega(int entrega_id) void
        +get_entregas_dia() List~Entrega~
    }

    class Rota {
        -int id
        -String origem
        -String destino
        -float distancia
        -int tempo_estimado
        +calcular_rota(String origem, String destino) Dict
    }

    Entrega "1" --> "0..*" StatusEntrega : Possui
    Entrega "1" --> "0..1" Entregador : Atribuida
    Entregador "1" --> "0..*" Rota : Utiliza
```

## 6.8 MÓDULO DE MULTI LOJAS
```mermaid
classDiagram
    class Loja {
        -int id
        -String nome
        -String cnpj
        -String endereco
        -String telefone
        -String pdv_sistema
        -String status_onboarding
        -int sugestoes_aceitas
        -int alertas_vencimento
        +cadastrar() bool
        +editar() bool
        +excluir() bool
        +ativar() void
        +desativar() void
    }

    class Transferencia {
        -int id
        -int produto_id
        -int loja_origem_id
        -int loja_destino_id
        -int quantidade
        -String motivo
        -String status
        -DateTime data
        +confirmar() bool
        +cancelar() bool
    }

    class ProdutoLoja {
        -int id
        -int produto_id
        -int loja_id
        -int quantidade
        -DateTime updated_at
        +transferir(int quantidade, Loja destino) bool
        +ajustar(int nova_quantidade) void
    }

    class RelatorioConsolidado {
        -int id
        -int loja_id
        -float total_vendas
        -int total_clientes
        -float total_faturamento
        -int total_produtos
        -DateTime data
        +gerar() Dict
        +comparar() Dict
    }

    Loja "1" --> "0..*" Transferencia : Envia/Recebe
    Loja "1" --> "0..*" ProdutoLoja : Possui
    Loja "1" --> "0..*" RelatorioConsolidado : Gera
    Produto "1" --> "0..*" ProdutoLoja : Distribui
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

    Plano Rede (Até 5 lojas integradas): R$ 499,00 por mês.

8.2. Investimento do MVP (Preço Fixo)

Para a construção, validação e estabilização do barramento Flask com banco SQLite que você possui no código, o valor comercial fechado do projeto está estipulado em R$ 120.000,00, com pagamentos atrelados aos seguintes marcos técnicos:

    30% na Entrada: UI completa + 21 módulos.

    30% na Entrega Intermediária: Banco de dados SQLite estruturado e rotas de CRUD operacionais.

    40% no Encerramento: Liberação do Dashboard Estratégicos + Analitico + Fidelidades + Insights + Alertas. 

    
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

