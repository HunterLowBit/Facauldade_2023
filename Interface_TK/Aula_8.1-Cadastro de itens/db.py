import sqlite3
def cria_db(produto, preco):
    conn = sqlite3.connect('produtos.db')
    bd = conn.cursor()
    bd.execute('CREATE TABLE IF NOT EXISTS Cadastro (id INTEGER PRIMARY KEY AUTOINCREMENT, produto VARCHAR(100), preço REAL NOT NULL, descricao VARCHAR(200), fk_categoria INTEGER)')
    bd.execute("INSERT INTO produtos (produto, preço) VALUES (?,?)",(produto,preco))
    conn.commit()
    conn.close()