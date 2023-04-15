import tkinter as tk

def sair():
    janela.quit()

janela = tk.Tk()

# Criar o menubar
menubar = tk.Menu(janela)
janela.config(menu=menubar)

# Criar o menu "Arquivo"
menu_arquivo = tk.Menu(menubar, tearoff=False)
menu_arquivo.add_command(label="Abrir")
menu_arquivo.add_command(label="Salvar")
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

# Criar a área de texto
texto = tk.Text(janela)
texto.grid(row=0, column=0, sticky="nsew")

# Adicionar a barra de rolagem ao texto
scrollbar = tk.Scrollbar(janela, command=texto.yview)
scrollbar.grid(row=0, column=1, sticky="nsew")
texto.config(yscrollcommand=scrollbar.set)

janela.mainloop()
