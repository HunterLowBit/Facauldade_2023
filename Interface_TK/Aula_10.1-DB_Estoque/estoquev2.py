#pip install psycopg2
import tkinter as tk
import psycopg2

# Função para adicionar um usuário ao banco de dados
def adicionar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(
            host="babar.db.elephantsql.com",
            database="Estoque",
            user="rsstmgaf",
            password="f_vbIwweAPOMnavixW7kDKu9oKrZasb5"
        )
        
        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()
        
        # Inserir dados do usuário na tabela
        sql = "INSERT INTO users (nome, email) VALUES (%s, %s)"
        val = (nome, email)
        cursor.execute(sql, val)
        
        # Commit das alterações no banco de dados
        conn.commit()
        
        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()
        
        # Limpar os campos de entrada
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        
        # Exibir uma mensagem de sucesso
        label_status["text"] = "Usuário adicionado com sucesso!"
        label_status["fg"] = "green"
        
    except (Exception, psycopg2.DatabaseError) as error:
        # Exibir uma mensagem de erro
        label_status["text"] = "Erro ao adicionar usuário: " + str(error)
        label_status["fg"] = "red"

# Criar a janela Tkinter
window = tk.Tk()
window.title("Cadastro de Usuários")
window.geometry("400x400")

# Criar rótulos e campos de entrada para o nome e email do usuário
label_nome = tk.Label(window, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(window)
entry_nome.pack()

label_email = tk.Label(window, text="Email:")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

# Botão para adicionar usuário
button_adicionar = tk.Button(window, text="Adicionar Usuário", command=adicionar_usuario)
button_adicionar.pack()

# Label para exibir o status
label_status = tk.Label(window, text="")
label_status.pack()

# Iniciar a janela Tkinter
window.mainloop()

