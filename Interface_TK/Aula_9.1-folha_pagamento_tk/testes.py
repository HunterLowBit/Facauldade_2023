# Criar um minisistema de calculo de folha de pagamento com tkinter. Com menus + regra de negócio do imposto de renda, inss e ect.
'''
Base de cálculo (R$)	Alíquota (%)	Parcela a deduzir (R$)
Até 1.903,98	            Isento	        Isento
De 1.903,99 até 2.826,65	7,5%	        R$ 142,80
De 2.826,66 até 3.751,05	15%	            R$ 354,80
De 3.751,06 até 4.664,68	22,5%	        R$ 636,13
Acima de 4.664,68	        27,5%	        R$ 869,36
'''

import tkinter.simpledialog as sd
import tkinter as tk
import tkinter.messagebox as msg_box
import sqlite3

# Cria o banco de dados SQLite
conn = sqlite3.connect('cadastro.db')
conn.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                salario TEXT NOT NULL,
                cargo TEXT NOT NULL)''')

# Função para adicionar um novo cliente


def adicionar_cliente():
    nome = entrada_nome.get()
    salario = entrada_salario.get()
    cargo = entrada_cargo.get()
    conn.execute(
        "INSERT INTO clientes (nome, salario, cargo) VALUES (?, ?, ?)", (nome, salario, cargo))
    conn.commit()
    listar_clientes()

# Função para remover um cliente pelo ID
def remover_id():
    consulta = conn.execute("SELECT * FROM clientes")
    cadastro = consulta.fetchall()
    if cadastro:
        cliente_id = msg_box.askquestion(
            "Remover ID", "Deseja realmente remover um cadastro por 'ID'?")
        if cliente_id == 'yes':
            cliente_id_str = sd.askstring(
                "Remover ID", "Digite o ID do produto que deseja remover:")
            try:
                cliente_id = int(cliente_id_str)  # type: ignore
                conn.execute(
                    "DELETE FROM clientes WHERE ID = ?", (cliente_id,))
                conn.commit()
            except ValueError:
                msg_box.showerror(title="Erro", message="ID inválido")
        else:
            msg_box.showwarning("Produtos Cadastrados",
                                "Nenhum produto cadastrado.")


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
        lista_clientes.insert(
            tk.END, f"{row[0]} | Nome: {row[1]} | Salario: {row[2]} | Cargo: {row[3]}")

# Cria a janela principal
janela = tk.Tk()

# Adiciona os widgets à janela
rotulo_nome = tk.Label(janela, text="Nome:")
entrada_nome = tk.Entry(janela)

rotulo_salario = tk.Label(janela, text="Salario:")
entrada_salario = tk.Entry(janela)

rotulo_cargo = tk.Label(janela, text="Cargo:")
entrada_cargo = tk.Entry(janela)

botao_adicionar = tk.Button(
    janela, text="Adicionar", command=adicionar_cliente)
botao_remover = tk.Button(janela, text="Remover", command=remover_cliente)


lista_clientes = tk.Listbox(janela)
listar_clientes()

# Menubar
menu_bar = tk.Menu(janela)

remover_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Remover", menu=remover_menu)
remover_menu.add_command(label="Remover por 'ID'", command=remover_id)

janela.config(menu=menu_bar)

# Define as propriedades dos widgets
janela.title("Cadastro de Clientes")
janela.geometry("400x300")

# Adiciona os widgets à janela
rotulo_nome.pack()
entrada_nome.pack()

rotulo_salario.pack()
entrada_salario.pack()

rotulo_cargo.pack()
entrada_cargo.pack()

botao_adicionar.pack(side=tk.LEFT)
botao_remover.pack(side=tk.RIGHT)

# expand=1 expanda todo o widget, enquanto fill
lista_clientes.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Inicia o loop principal da janela
janela.mainloop()

# Fecha a conexão com o banco de dados
conn.close()
