import tkinter as tk
import mysql.connector
import requests

# Função para recuperar dados da API do ElephantSQL
def recuperar_dados():
    url = "5d99dc28-e25d-4dae-a948-61db5ba431e0"  # Substitua pelo URL da sua API do ElephantSQL
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Exemplo: exibindo os dados em um label
        label_resultado["text"] = str(data)
    except requests.exceptions.RequestException as e:
        label_resultado["text"] = "Erro ao recuperar os dados da API."

# Função para conectar ao servidor MySQL
def conectar():
    global mydb
    
    # Conectar ao banco de dados
    mydb = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="mydatabase"
    )
    
    # Exibir uma mensagem de conexão bem-sucedida
    label_status["text"] = "Conectado ao servidor MySQL!"
    label_status["fg"] = "green"

# Função para adicionar um usuário ao banco de dados
def adicionar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    
    # Criar um cursor para executar comandos SQL
    cursor = mydb.cursor()
    
    # Inserir dados do usuário na tabela
    sql = "INSERT INTO users (nome, email) VALUES (%s, %s)"
    val = (nome, email)
    cursor.execute(sql, val)
    
    # Commit das alterações no banco de dados
    mydb.commit()
    
    # Limpar os campos de entrada
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    
    # Exibir uma mensagem de sucesso
    label_status["text"] = "Usuário adicionado com sucesso!"
    label_status["fg"] = "green"

# Criar a janela Tkinter
window = tk.Tk()
window.title("Cadastro de Usuários")
window.geometry("400x400")

# Botão para conectar ao servidor MySQL
button_conectar = tk.Button(window, text="Conectar", command=conectar)
button_conectar.pack()

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

# Botão para recuperar dados da API
button_recuperar = tk.Button(window, text="Recuperar Dados", command=recuperar_dados)
button_recuperar.pack()

# Label para exibir o resultado
label_resultado = tk.Label(window, text="")
label_resultado.pack()

# Iniciar a janela Tkinter
window.mainloop()