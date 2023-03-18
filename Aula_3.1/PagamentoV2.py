class Folha_Pagamento:
    def __init__(self, Sbruto, Htrabalhadas):
        self.__Sbruto = Sbruto
        self.Htrabalhadas = Htrabalhadas


    def get_Sbruto(self):
        return self.__Sbruto

    def set_Sbruto(self, Sbruto):
        self.__Sbruto = Sbruto

    def get_horas_trabalhadas(self):
        return self.Htrabalhadas

    def set_horas_trabalhadas(self, Htrabalhadas):
        self.Htrabalhadas = Htrabalhadas


    def calcula_Sliquido(self):
        salario_liquido = self.__Sbruto
        inss = 0.07 if salario_liquido > 2000 else 0.05
        desconto_inss = salario_liquido * inss
        salario_liquido -= desconto_inss
        return salario_liquido

    def Calcula_inss(self):
        Sbruto = self.__Sbruto
        inss = 0.07 if Sbruto > 2000 else 0.05
        desconto_inss = Sbruto * inss
        return desconto_inss

funcionario1 = Folha_Pagamento(5000, 300)
salario_liquido = funcionario1.calcula_Sliquido()
desconto_inss = funcionario1.Calcula_inss()

print(f'\nSalário líquido: R$ {salario_liquido:.2f}\nDesconto do INSS: R$ {desconto_inss:.2f}')

funcionario2 = Folha_Pagamento(1500, 110)
salario_liquido = funcionario2.calcula_Sliquido()
desconto_inss = funcionario2.Calcula_inss()

print(f'\nSalário líquido: R$ {salario_liquido:.2f}\nDesconto do INSS: R$ {desconto_inss:.2f}')