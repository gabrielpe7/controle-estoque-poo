import sqlite3

ARQUIVO = "estoque.db"

def criar_tabela():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()
    
def inserir_produto(produto):
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
        (produto.nome, produto.preco, produto.quantidade)
    )
    conexao.commit()
    conexao.close()
    
from produto import Produto

def listar_produtos_bd():
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
    resultados = cursor.fetchall()
    conexao.close()
    
    lista_de_produtos = []
    
    for id_produto, nome, preco, quantidade in resultados:
        produto = Produto(nome, preco, quantidade)
        produto.id = id_produto
        lista_de_produtos.append(produto)
        
    return lista_de_produtos

def atualizar_quantidade(id_produto, nova_quantidade):
    conexao = sqlite3.connect(ARQUIVO)
    cursor = conexao.cursor()
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))
    conexao.commit()
    conexao.close()