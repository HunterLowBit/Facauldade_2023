import time
class Humano:
    def __init__(self, nome, cor, roupa, vida):
        self.nome = nome
        self.cor = cor
        self.roupa = roupa
        self.vida = vida

Nomejogador = input("Bem-vindo,\nQual o nome de seu personagem? ")

jogador = Humano (Nomejogador, "Cinza", "Polo", 10)
inimigo1 = Humano ("Lord","Branco","Sobretudo", 15)
inimigo2 = Humano ("Ryder","Preto","Camiseta", 20)

print(
    f"Seu nome é {jogador.nome} \nPossui cor de cabelo {jogador.cor} \nVestindo {jogador.roupa}"
)
time.sleep(2)
print("Existe apenas duas pessoas em seu compo de visão\n")
time.sleep(1.5)
print(
    f"A que esta mais longe se chama {inimigo2.nome}\n"
)
time.sleep(1.5)
print(
    f"possuindo cabelo {inimigo2.cor}\n"
)
time.sleep(1.5)
print(
    f"vestindo apenas {inimigo2.roupa}.\n"
)
time.sleep(1.5)
print(
    f"A mais proxima se chama {inimigo1.nome}\n"
)
time.sleep(1.5)
print(
    f"possuindo cabelo {inimigo1.cor}\n"
)
time.sleep(1.5)
print(
    f"vestindo apenas {inimigo1.roupa}.\n o que deseja fazer?\n"
)
print("\n             |-> Sair \nA   S    D   Q \n|   |__  |____ \n|      |      | \nAndar Falar Bater \n")  #Normal   
