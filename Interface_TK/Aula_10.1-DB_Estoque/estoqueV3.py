import tkinter as tk
import sqlite3
from tkinter import messagebox

# Função para criar a tabela de estoque
def criar_tabela_estoque():
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       preco REAL NOT NULL,
                       quantidade INTEGER NOT NULL)''')

    conexao.commit()
    conexao.close()

# Função para inserir um produto no estoque
def inserir_produto():
    nome = entry_nome.get()
    preco = float(entry_preco.get())
    quantidade = int(entry_quantidade.get())

    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))

    conexao.commit()
    conexao.close()

    # Limpar os campos de entrada após a inserção
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

    atualizar_lista_produtos()

# Função para consultar todos os produtos do estoque
def consultar_produtos():
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
    produtos = cursor.fetchall()

    conexao.close()

    return produtos

# Função para atualizar a lista de produtos exibida na tela
def atualizar_lista_produtos():
    lista_produtos.delete(0, tk.END)

    produtos = consultar_produtos()
    for produto in produtos:
        lista_produtos.insert(tk.END, f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:.2f} | Quantidade: {produto[3]}")

# Função para atualizar o preço de um produto (apenas para o admin)
def atualizar_preco_produto():
    id_produto = int(entry_id_produto.get())
    novo_preco = float(entry_novo_preco.get())

    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (novo_preco, id_produto))

    conexao.commit()
    conexao.close()

    # Limpar os campos de entrada após a atualização
    entry_id_produto.delete(0, tk.END)
    entry_novo_preco.delete(0, tk.END)

    atualizar_lista_produtos()

# Função para remover um produto (apenas com a senha do admin)
def remover_produto():
    senha = entry_senha.get()
    if senha == "admin123":
        id_produto = int(entry_id_produto.get())

        conexao = sqlite3.connect('estoque.db')
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

        conexao.commit()
        conexao.close()

        # Limpar os campos de entrada após a remoção
        entry_id_produto.delete(0, tk.END)
        entry_senha.delete(0, tk.END)

        atualizar_lista_produtos()
    else:
        messagebox.showwarning("Acesso Negado", "Senha do administrador incorreta.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Controlede Estoque")
janela.geometry("300x500")


label_nome = tk.Label(janela, text="Nome do Produto:")
label_nome.grid(row=0, column=0, sticky=tk.W)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

label_preco = tk.Label(janela, text="Preço:")
label_preco.grid(row=1, column=0, sticky=tk.W)

entry_preco = tk.Entry(janela)
entry_preco.grid(row=1, column=1)

label_quantidade = tk.Label(janela, text="Quantidade:")
label_quantidade.grid(row=2, column=0, sticky=tk.W)

entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=2, column=1)

btn_inserir = tk.Button(janela, text="Inserir Produto", command=inserir_produto)
btn_inserir.grid(row=3, column=0, columnspan=2, pady=10)


lista_produtos = tk.Listbox(janela)
lista_produtos.grid(row=4, column=0, columnspan=2, padx=10)


label_id_produto = tk.Label(janela, text="ID do Produto:")
label_id_produto.grid(row=5, column=0, sticky=tk.W)

entry_id_produto = tk.Entry(janela)
entry_id_produto.grid(row=5, column=1)

label_novo_preco = tk.Label(janela, text="Novo Preço:")
label_novo_preco.grid(row=6, column=0, sticky=tk.W)

entry_novo_preco = tk.Entry(janela)
entry_novo_preco.grid(row=6, column=1)

btn_atualizar_preco = tk.Button(janela, text="Atualizar Preço", command=atualizar_preco_produto)
btn_atualizar_preco.grid(row=7, column=0, columnspan=2, pady=10)


label_senha = tk.Label(janela, text="Senha do Admin:")
label_senha.grid(row=8, column=0, sticky=tk.W)

entry_senha = tk.Entry(janela, show="*")
entry_senha.grid(row=8, column=1)

btn_remover_produto = tk.Button(janela, text="Remover Produto", command=remover_produto)
btn_remover_produto.grid(row=10, column=0, columnspan=2, pady=10)


atualizar_lista_produtos()


janela.mainloop()
