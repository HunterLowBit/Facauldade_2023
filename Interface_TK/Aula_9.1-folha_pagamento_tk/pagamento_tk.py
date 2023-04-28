import tkinter as tk
import tkinter.messagebox as msg_box
# Função para calcular o desconto 
def calcular_desconto():
    salario = float(entrada_salario.get())
    nome = str(entrada_nome.get())

    if salario <= 1903.98:
        desconto_ir = 0
    elif salario <= 2826.65:
        desconto_ir = (salario * 0.075) - 142.80
    elif salario <= 3751.05:
        desconto_ir = (salario * 0.15) - 354.80
    elif salario <= 4664.68:
        desconto_ir = (salario * 0.225) - 636.13
    else:
        desconto_ir = (salario * 0.275) - 869.36
        
    desconto_alimentacao = salario * 0.01

    vale_transporte = salario * 0.06
       
    desconto_inss = salario * 0.11
    salario_liquido = salario - desconto_ir - desconto_inss - desconto_alimentacao
    
    n_liquido = salario_liquido - vale_transporte

    msg_box.showinfo(title="Desconto de Folha de Pagamento", 
                     message=f"""
Nome: {nome}          
Salário: R$ {salario:.2f}
__________________________________
Desconto IR: R$ {desconto_ir:.2f}
Desconto INSS: R$ {desconto_inss:.2f}
Desconto Vale-Refeição: R$ {desconto_alimentacao:.2f}
___________________________________
Salário Líquido: R$ {salario_liquido:.2f}
Vale-Transporte: R$ {vale_transporte:.2f}
__________________________________
Salário Líquido Final: R$ {n_liquido:.2f}""")

# Cria a janela principal
janela = tk.Tk()

# Adiciona os widgets à janela
rotulo_nome = tk.Label(janela, text="Nome:")
entrada_nome = tk.Entry(janela)

rotulo_salario = tk.Label(janela, text="Salario:")
entrada_salario = tk.Entry(janela)

# Menubar
menu_bar = tk.Menu(janela)

calcular_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Calcular Desconto", menu=calcular_menu)
calcular_menu.add_command(label="Calcular", command=calcular_desconto)

janela.config(menu=menu_bar)

# Define as propriedades dos widgets
janela.title("Cadastro de Clientes")
janela.geometry("300x100")

# Adiciona os widgets à janela
rotulo_nome.pack()
entrada_nome.pack()

rotulo_salario.pack()
entrada_salario.pack()

# Inicia o loop principal da janela
janela.mainloop()