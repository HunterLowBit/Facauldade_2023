import tkinter.simpledialog as sd
import tkinter as tk
import tkinter.messagebox as msg_box
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


def exibir_produtos():
    consulta = conn.execute("SELECT * FROM produtos")
    produtos = consulta.fetchall()
    if produtos:
        msg_box.showinfo("Produtos Cadastrados", produtos)  # type: ignore
    else:
        msg_box.showwarning("Produtos Cadastrados",
                            "Nenhum produto cadastrado.")


def remover_produto():
    consulta = conn.execute("SELECT * FROM produtos")
    produtos = consulta.fetchall()
    if produtos:
        produto_id = msg_box.askquestion(
            "Remover Produto", "Deseja realmente remover um produto?")
        if produto_id == 'yes':
            produto_id_str = sd.askstring(
                "Remover Produto", "Digite o ID do produto que deseja remover:")
            try:
                produto_id = int(produto_id_str)
                conn.execute(
                    "DELETE FROM produtos WHERE ID = ?", (produto_id,))
                conn.commit()
                status_label.configure(text="Produto removido com sucesso!")
            except ValueError:
                status_label.configure(text="ID do produto inválido.")
        else:
            status_label.configure(text="Remoção de produto cancelada.")
    else:
        msg_box.showwarning("Produtos Cadastrados",
                            "Nenhum produto cadastrado.")


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

consultar_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Consultar", menu=consultar_menu)
consultar_menu.add_command(label="Exibir Produtos", command=exibir_produtos)

remover_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Remover", menu=remover_menu)
remover_menu.add_command(label="Remover Produto", command=remover_produto)

janela.config(menu=menu_bar)

janela.mainloop()

conn.close()
