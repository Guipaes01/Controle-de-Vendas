import psycopg2
from faker import Faker
from datetime import datetime
import random

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="Estoque",
    user="USUARIO",
    password="SENHA"
)
cursor = conn.cursor()
fake = Faker('pt_BR')

# Função para criar clientes
def criar_clientes(n=20):
    clientes = []
    for _ in range(n):
        nome = fake.name()
        email = fake.email()
        telefone = fake.phone_number()
        data_cadastro = fake.date_time_this_decade()
        status = random.choice(['ativo', 'inativo'])
        cursor.execute("""
            INSERT INTO clientes (nome, email, contato, data_cadastro, status)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        """, (nome, email, telefone, data_cadastro, status))
        clientes.append(cursor.fetchone()[0])
    return clientes

# Função para criar mesas
def criar_mesas(n=10):
    mesas = []
    for i in range(1, n + 1):
        nome = f"Mesa {i}"
        status = random.choice(['livre', 'ocupada', 'reservada'])
        cursor.execute("""
            INSERT INTO mesas (nome, status)
            VALUES (%s, %s) RETURNING id
        """, (nome, status))
        mesas.append(cursor.fetchone()[0])
    return mesas

# Função para criar produtos
def criar_produtos(n=15):
    categorias = ['Bebida', 'Lanche', 'Sobremesa', 'Prato Principal']
    produtos = []
    for _ in range(n):
        nome = fake.word().capitalize()
        categoria = random.choice(categorias)
        preco = round(random.uniform(20.0, 100.0), 2)
        custo = round(random.uniform(10.0, preco - 1), 2)
        cursor.execute("""
            INSERT INTO produtos (nome, categoria, preco, custo_unitario)
            VALUES (%s, %s, %s, %s) RETURNING id
        """, (nome, categoria, preco, custo))
        produtos.append(cursor.fetchone()[0])
    return produtos

# Função para criar pedidos
def criar_pedidos(clientes, mesas, n=30):
    pedidos = []
    for _ in range(n):
        cliente_id = random.choice(clientes)
        mesa_id = random.choice(mesas)
        data = fake.date_time_this_year()
        status = random.choice(['aberto', 'fechado', 'cancelado'])
        total = round(random.uniform(20, 300), 2)
        cursor.execute("""
            INSERT INTO pedidos (data, id_cliente, id_mesa, status, total)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        """, (data, cliente_id, mesa_id, status, total))
        pedidos.append(cursor.fetchone()[0])
    return pedidos

# Função para criar itens de pedido
def criar_itens_pedido(pedidos, produtos):
    for pedido_id in pedidos:
        for _ in range(random.randint(1, 5)):
            produto_id = random.choice(produtos)
            quantidade = random.randint(1, 4)
            valor_unitario = round(random.uniform(5.0, 80.0), 2)
            cursor.execute("""
                INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, valor_unitario)
                VALUES (%s, %s, %s, %s)
            """, (pedido_id, produto_id, quantidade, valor_unitario))

# Função para criar pagamentos
def criar_pagamentos(pedidos):
    formas = ['dinheiro', 'cartão', 'pix']
    for pedido_id in pedidos:
        forma_pagamento = random.choice(formas)
        valor = round(random.uniform(20, 300), 2)
        cursor.execute("""
            INSERT INTO pagamentos (id_pedido, forma_pagamento, valor_pago)
            VALUES (%s, %s, %s)
        """, (pedido_id, forma_pagamento, valor))

# Função para criar reservas
def criar_reservas(clientes, mesas, n=15):
    for _ in range(n):
        cliente_id = random.choice(clientes)
        mesa_id = random.choice(mesas)
        data_reserva = fake.date_time_between(start_date='-30d', end_date='+30d')
        status = random.choice(['confirmada', 'cancelada', 'pendente'])
        cursor.execute("""
            INSERT INTO reservas (id_cliente, id_mesa, data_reserva, status)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, mesa_id, data_reserva, status))

# Execução principal
clientes = criar_clientes()
mesas = criar_mesas()
produtos = criar_produtos()
pedidos = criar_pedidos(clientes, mesas)
criar_itens_pedido(pedidos, produtos)
criar_pagamentos(pedidos)
criar_reservas(clientes, mesas)

# Finalizar
conn.commit()
cursor.close()
conn.close()
print("✅ Dados fictícios inseridos com sucesso em todas as tabelas.")
