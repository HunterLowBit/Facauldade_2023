import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def sair():
    root.quit()

def salvar_como():
    arquivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt"), ("Todos os arquivos", "*.*")])
    if arquivo:
        conteudo = texto.get("1.0", "end-1c")
        arquivo.write(conteudo)
        arquivo.close()
        messagebox.showinfo("Aviso", "Arquivo salvo com sucesso!")

def abrir_arquivo():
    messagebox.showinfo('ALERTA','Qualquer mudança será perdida\ncaso não tenha salvo!')
    arquivo = filedialog.askopenfile(filetypes=[("Arquivo de Texto", "*.txt"), ("Todos os arquivos", "*.*")])
    if arquivo:
        conteudo = arquivo.read()
        texto.delete("1.0", "end")
        texto.insert("1.0", conteudo)
        arquivo.close()

def copiar():
    texto.clipboard_clear()
    texto.clipboard_append(texto.selection_get())

def recortar():
    texto.clipboard_clear()
    texto.clipboard_append(texto.selection_get())
    texto.delete("sel.first", "sel.last")

def colar():
    texto.insert("insert", texto.clipboard_get())        

root = tk.Tk()

# Criar o menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Criar o menu "Arquivo"
menu_arquivo = tk.Menu(menubar, tearoff=False)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_como)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

# Criar o menu "Editar"
menu_editar = tk.Menu(menubar, tearoff=False)
menu_editar.add_command(label="Copiar(CTRL+C)", command=copiar)
menu_editar.add_command(label="Recortar(CTRL+X)", command=recortar)
menu_editar.add_command(label="Colar(CTR+C)", command=colar)
menubar.add_cascade(label="Editar", menu=menu_editar)

# Criar a área de texto
texto = tk.Text(root)
texto.grid(row=0, column=0, sticky="nsew")

# Adicionar a barra de rolagem ao texto
scrollbar = tk.Scrollbar(root, command=texto.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
texto.config(yscrollcommand=scrollbar.set)

root.mainloop()
