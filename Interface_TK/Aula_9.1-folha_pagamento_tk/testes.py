# Criar um minisistema de calculo de folha de pagamento com tkinter. Com menus + regra de negócio do imposto de renda, inss e ect.
'''
Base de cálculo (R$)	Alíquota (%)	Parcela a deduzir (R$)
Até 1.903,98	            Isento	        Isento
De 1.903,99 até 2.826,65	7,5%	        R$ 142,80
De 2.826,66 até 3.751,05	15%	            R$ 354,80
De 3.751,06 até 4.664,68	22,5%	        R$ 636,13
Acima de 4.664,68	        27,5%	        R$ 869,36
'''


import sqlite3
import tkinter as tk

# Cria o banco de dados SQLite
conn = sqlite3.connect('cadastro.db')
conn.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL)''')

# Função para adicionar um novo cliente
def adicionar_cliente():
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    conn.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    listar_clientes()

# Função para remover um cliente pelo ID
def remover_cliente():
    id = lista_clientes.curselection()[0]+1
    conn.execute("DELETE FROM clientes WHERE id=?", (id,))
    conn.commit()
    listar_clientes()

# Função para listar todos os clientes
def listar_clientes():
    lista_clientes.delete(0, tk.END)
    cursor = conn.execute("SELECT * FROM clientes")
    for row in cursor:
        lista_clientes.insert(tk.END, f"{row[0]} | Nome: {row[1]} | Telefone: {row[2]} | Email: {row[3]}")

# Cria a janela principal
janela = tk.Tk()

# Adiciona os widgets à janela
rotulo_nome = tk.Label(janela, text="Nome:")
entrada_nome = tk.Entry(janela)

rotulo_telefone = tk.Label(janela, text="Telefone:")
entrada_telefone = tk.Entry(janela)

rotulo_email = tk.Label(janela, text="Email:")
entrada_email = tk.Entry(janela)

botao_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_cliente)
botao_remover = tk.Button(janela, text="Remover", command=remover_cliente)

lista_clientes = tk.Listbox(janela)
listar_clientes()

# Define as propriedades dos widgets
janela.title("Cadastro de Clientes")
janela.geometry("300x300")

# Adiciona os widgets à janela
rotulo_nome.pack()
entrada_nome.pack()

rotulo_telefone.pack()
entrada_telefone.pack()

rotulo_email.pack()
entrada_email.pack()

botao_adicionar.pack(side=tk.LEFT)
botao_remover.pack(side=tk.RIGHT)

lista_clientes.pack(side=tk.TOP, fill=tk.BOTH, expand=1)  # expand=1 expanda todo o widget, enquanto fill

# Inicia o loop principal da janela
janela.mainloop()

# Fecha a conexão com o banco de dados
conn.close()
