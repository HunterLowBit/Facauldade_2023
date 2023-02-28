class Salario:
    def __init__(self, Vhora):
        self.Vhora = Vhora
        self.__Sbruto = 0
        self.__Htrabalhada = 0
        self.__Sliquido = 0
#Salario =< 2000 -> 5%, > 2000 -> 7%      
    @property
    def Sbruto(self):
        return self.__Sbruto
    
    @Sbruto.setter
    def Sbruto(self, Novo_Sbruto):
        raise ValueError("")
    
    def Registrar_Htrabalhada(self):
        self.__Htrabalhada += 1
        
    def Calcula_Sbruto(self):
        self.__Sbruto = self.__Htrabalhada * Vhora
        
a = Salario(5)
a.Registrar_Htrabalhada()
a.Calcula_Sbruto
print(a.Sbruto)