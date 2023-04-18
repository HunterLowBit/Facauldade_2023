import tkinter as tk
import sqlite3

conn = sqlite3.connect('produtos.db')
conn.execute('''CREATE TABLE IF NOT EXISTS produtos
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NOME TEXT NOT NULL,
             PRECO REAL NOT NULL);''')


def cadastrar_produto():
    nome = nome_entry.get()
    preco = preco_entry.get()
    conn.execute(
        "INSERT INTO produtos (NOME, PRECO) VALUES (?, ?)", (nome, preco))
    conn.commit()
    status_label.configure(text="Produto cadastrado com sucesso!")


def consultar_produtos():
    consulta = conn.execute("SELECT * FROM produtos")
    produtos = consulta.fetchall()
    for produto in produtos:
        print(produto)


def remover_produto():
    id_produto = int(input("Digite o ID do produto a ser removido: "))
    conn.execute("DELETE FROM produtos WHERE ID = ?", (id_produto,))
    conn.commit()
    print("Produto removido com sucesso!")


janela = tk.Tk()
janela.title("Cadastro de Produtos")

nome_label = tk.Label(janela, text="Nome do Produto")
nome_label.grid(row=0, column=0)

nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1)

preco_label = tk.Label(janela, text="Preço do Produto")
preco_label.grid(row=1, column=0)

preco_entry = tk.Entry(janela)
preco_entry.grid(row=1, column=1)

cadastrar_button = tk.Button(
    janela, text="Cadastrar", command=cadastrar_produto)
cadastrar_button.grid(row=2, column=0)

status_label = tk.Label(janela, text="")
status_label.grid(row=2, column=1)

menu_bar = tk.Menu(janela)
janela.config(menu=menu_bar)

consulta_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Consultar", menu=consulta_menu)
consulta_menu.add_command(label="Produtos Cadastrados",
                          command=consultar_produtos)

remocao_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Remover", menu=remocao_menu)
remocao_menu.add_command(label="Remover Produto", command=remover_produto)

janela.mainloop()
