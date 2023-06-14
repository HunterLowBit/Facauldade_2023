import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
from tkinter import messagebox

# Constantes
ADB_PATH = os.path.join(os.path.dirname(__file__), "adb", "adb.exe")
WINDOW_TITLE = "Aplicação ADB"
WINDOW_SIZE = "400x250"
LABEL_ORIGEM_TEXT = "Pasta de origem:"
LABEL_DESTINO_TEXT = "Pasta de destino:"
BTN_ORIGEM_TEXT = "Abrir pasta de origem"
BTN_DESTINO_TEXT = "Abrir pasta de destino"
BTN_PULL_TEXT = "Executar adb pull"
BTN_PUSH_TEXT = "Executar adb push"
BTN_DEVICES_TEXT = "adb devices"
LOG_WINDOW_TITLE = "Log de Progresso"
LOG_WIDTH = 50
LOG_HEIGHT = 10
ERROR_TITLE = "Erro"

def executar_comando_adb(comando):
    resultado = subprocess.run([ADB_PATH] + comando, capture_output=True, text=True)
    if resultado.returncode != 0:
        print(f"Erro: {resultado.stderr}")
    return resultado.stdout

def abrir_pasta(title):
    pasta = filedialog.askdirectory()
    return pasta

def mostrar_mensagem_erro(titulo, mensagem):
    messagebox.showerror(titulo, mensagem)

def executar_pull():
    origem = entry_origem.get()
    destino = entry_destino.get()
    
    if not origem or not destino:
        mostrar_mensagem_erro(ERROR_TITLE, "Por favor, preencha os campos de origem e destino.")
        return
    
    if not os.path.exists(origem):
        mostrar_mensagem_erro(ERROR_TITLE, "A pasta de origem não existe.")
        return
    
    if not os.path.exists(destino):
        mostrar_mensagem_erro(ERROR_TITLE, "A pasta de destino não existe.")
        return
    
    resultado_ls = executar_comando_adb(["adb", "shell", "ls", origem])
    arquivos = resultado_ls.splitlines()
    
    if not arquivos:
        mostrar_mensagem_erro(ERROR_TITLE, "Erro ao obter a lista de arquivos.")
        return
    
    tamanho_total = len(arquivos)
    progresso["maximum"] = tamanho_total
    
    log_text.configure(state=tk.NORMAL)
    log_text.delete(1.0, tk.END)
    
    for arquivo in arquivos:
        comando_arquivo = ["adb", "pull", os.path.join(origem, arquivo), destino]
        resultado_pull = executar_comando_adb(comando_arquivo)
        log_text.insert(tk.END, resultado_pull + "\n")
        progresso["value"] += 1
    
    log_text.configure(state=tk.DISABLED)

def executar_push():
    origem = entry_origem.get()
    destino = entry_destino.get()
    
    if not origem or not destino:
        mostrar_mensagem_erro(ERROR_TITLE, "Por favor, preencha os campos de origem e destino.")
        return
    
    if not os.path.exists(origem):
        mostrar_mensagem_erro(ERROR_TITLE, "A pasta de origem não existe.")
        return
    
    if not os.path.exists(destino):
        mostrar_mensagem_erro(ERROR_TITLE, "A pasta de destino não existe.")
        return
    
    comando = ["adb", "push", origem, destino]
    resultado_push = executar_comando_adb(comando)
    print(resultado_push)

def executar_devices():
    resultado_devices = executar_comando_adb(["adb", "devices"])
    dispositivos = resultado_devices.splitlines()[1:]
    
    dispositivos_window = tk.Toplevel(window)
    dispositivos_window.title("Dispositivos")
    dispositivos_text = tk.Text(dispositivos_window, width=50, height=10)
    dispositivos_text.pack()
    
    dispositivos_text.insert(tk.END, "\n".join(dispositivos))

# Criação da janela Tkinter
window = tk.Tk()
window.title(WINDOW_TITLE)
window.geometry(WINDOW_SIZE)

# Rótulos e entradas de texto
label_origem = tk.Label(window, text=LABEL_ORIGEM_TEXT)
label_origem.pack()
entry_origem = tk.Entry(window, width=50)
entry_origem.pack()

label_destino = tk.Label(window, text=LABEL_DESTINO_TEXT)
label_destino.pack()
entry_destino = tk.Entry(window, width=50)
entry_destino.pack()

# Botões
btn_origem = tk.Button(window, text=BTN_ORIGEM_TEXT, command=lambda: entry_origem.insert(0, abrir_pasta("Selecionar pasta de origem")))
btn_origem.pack()

btn_destino = tk.Button(window, text=BTN_DESTINO_TEXT, command=lambda: entry_destino.insert(0, abrir_pasta("Selecionar pasta de destino")))
btn_destino.pack()

btn_pull = tk.Button(window, text=BTN_PULL_TEXT, command=executar_pull)
btn_pull.pack()

btn_push = tk.Button(window, text=BTN_PUSH_TEXT, command=executar_push)
btn_push.pack()

btn_devices = tk.Button(window, text=BTN_DEVICES_TEXT, command=executar_devices)
btn_devices.pack()

# Barra de progresso
progresso = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progresso.pack()

# Log de progresso
log_text = tk.Text(window, width=LOG_WIDTH, height=LOG_HEIGHT, state=tk.DISABLED)
log_text.pack()

# Inicia o loop principal da janela Tkinter
window.mainloop()
#localidade do adb adb/adb.exe
#caminho adb pull "sdcard/Download/adb" "R:/adb/"