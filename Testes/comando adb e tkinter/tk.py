import subprocess
import tkinter as tk
from tkinter import filedialog

def executar_comando_adb(comando):
    # Executa o comando adb usando subprocess
    resultado = subprocess.run(comando, capture_output=True, text=True)
    
    # Verifica se houve erro na execução do comando
    if resultado.returncode != 0:
        print(f"Erro: {resultado.stderr}")
    
    # Retorna a saída padrão do comando
    return resultado.stdout

def adb_pull(origem, destino):
    # Executa o comando adb pull
    comando = ["adb", "pull", origem, destino]
    return executar_comando_adb(comando)

def adb_push(origem, destino):
    # Executa o comando adb push
    comando = ["adb", "push", origem, destino]
    return executar_comando_adb(comando)

def abrir_pasta_origem():
    # Abre a janela de diálogo para selecionar a pasta de origem
    pasta_origem = filedialog.askdirectory()
    if pasta_origem:
        entry_origem.delete(0, tk.END)
        entry_origem.insert(0, pasta_origem)

def abrir_pasta_destino():
    # Abre a janela de diálogo para selecionar a pasta de destino
    pasta_destino = filedialog.askdirectory()
    if pasta_destino:
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, pasta_destino)

def executar_pull():
    origem = entry_origem.get()
    destino = entry_destino.get()
    resultado_pull = adb_pull(origem, destino)
    print(resultado_pull)

def executar_push():
    origem = entry_origem.get()
    destino = entry_destino.get()
    resultado_push = adb_push(origem, destino)
    print(resultado_push)

# Criação da janela Tkinter
window = tk.Tk()
window.title("Aplicação ADB")
window.geometry("400x200")

# Rótulos e entradas de texto
label_origem = tk.Label(window, text="Pasta de origem:")
label_origem.pack()
entry_origem = tk.Entry(window, width=50)
entry_origem.pack()

label_destino = tk.Label(window, text="Pasta de destino:")
label_destino.pack()
entry_destino = tk.Entry(window, width=50)
entry_destino.pack()

# Botões
btn_origem = tk.Button(window, text="Abrir pasta de origem", command=abrir_pasta_origem)
btn_origem.pack()

btn_destino = tk.Button(window, text="Abrir pasta de destino", command=abrir_pasta_destino)
btn_destino.pack()

btn_pull = tk.Button(window, text="Executar adb pull", command=executar_pull)
btn_pull.pack()

btn_push = tk.Button(window, text="Executar adb push", command=executar_push)
btn_push.pack()

# Inicia o loop principal da janela Tkinter
window.mainloop()
