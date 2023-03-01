class Salario:
    def __init__(self, Htrabalhada, Sbruto):

        self.__Sbruto = Sbruto
        self.__Htrabalhada = Htrabalhada
        self.__Sliquido = 0
#Salario =< 2000 -> 5%, > 2000 -> 7%      
    @property
    def Sbruto(self):
        return self.__Sbruto
    
    @Sbruto.setter
    def Sbruto(self, Sbruto):
        self.__Sbruto = Sbruto
        

    
    def Registrar_Htrabalhada(self):
        self.__Htrabalhada += 1
        
    def Calcula_Sbruto(self):
        self.__Sbruto = self.__Htrabalhada * __Htrabalhada
        
a = Salario(5, )
a.Registrar_Htrabalhada()
a.Calcula_Sbruto
print(a.Sbruto)