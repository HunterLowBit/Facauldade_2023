class cachorro:
    def __init__(self, nome, raça, cor_do_pelo):
        self.nome = nome
        self.raça = raça
        self.cor_pelo_pelo = cor_do_pelo
        
    def quero_carinho(self):
        print( f"\ndando carinho a {self.nome}\n")
        
    def pular(self):
        print( f"{self.nome} pulou em você\n")
        
    def correr(self):
        print( f"{self.nome} está correndo\n")
        
    def Latir(self):
        print( f"{self.nome} começou a latir\n")
        
    def atributos(self):
        print(f"\no Nome é {self.nome}, a cor do pelo é {self.cor_pelo_pelo} e de raça {self.raça}\n")

bob = cachorro("Bob","Labrador","Laranja")
bob.quero_carinho()

lessy = cachorro("Lessy","Viralata","Caramelo")
lessy.correr()
lessy.Latir()
bob.pular()
bob.atributos()
lessy.atributos()