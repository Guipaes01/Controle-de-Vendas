# 📊 Sistema de Controle de Vendas e Financeiro com Power BI e PostgreSQL

Este projeto tem como objetivo centralizar, analisar e visualizar informações operacionais e financeiras relacionadas a vendas, pedidos, pagamentos e clientes, com **dados fictícios gerados via Python** e visualizações interativas no **Power BI**.

## 📌 Visão Geral do Projeto

O sistema simula um ambiente de vendas realista e permite análises estratégicas através de dashboards dinâmicos.

**Tecnologias utilizadas:**

* 🐘 **PostgreSQL** — Banco de dados relacional
* 🐍 **Python (Faker + psycopg2)** — Geração automática de dados
* 📊 **Power BI Desktop** — Visualização e análise de KPIs
* 🖥️ **Power Query + DAX** — Transformações e criação de medidas personalizadas  
* 🕒 Agendador de Tarefas do Windows — Automação da execução do script


---

## 📂 Estrutura do Projeto

### 🔧 Backend (Python + PostgreSQL)

Geração automática de dados para as seguintes tabelas:

* `clientes`: cadastro de clientes
* `mesas`: controle de mesas (livre, ocupada, reservada)
* `produtos`: catálogo de produtos por categoria
* `pedidos`: histórico de pedidos
* `itens_pedido`: detalhes dos itens vendidos por pedido
* `pagamentos`: formas de pagamento
* `reservas`: controle de reservas de mesas

> O script usado para injetar os dados está no arquivo:
> [`injetar_dados.py`](./injetar_dados.py)

### 🖥️ Power BI - Telas do Painel

#### 1. **Visão Geral**

* Total de Vendas
* Total de Pedidos
* Produtos Ativos
* Total de Clientes
* Evolução de Vendas por Mês
* Produtos Mais Vendidos
* Pedidos Recentes com status

#### 2. **Financeiro**

* Total Recebido
* Total Faturado
* Total em Aberto
* % de Inadimplência
* Custo Total
* Lucro Bruto
* Lucro Líquido
* Distribuição por Forma de Pagamento
* Gráfico de Vendas por Mês

---

## 🧑‍💻 Autor

**Guilherme Paes** - https://www.linkedin.com/in/paesgui/

