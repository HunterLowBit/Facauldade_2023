class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade


Pessoa1 = Pessoa("Jean Carlos", 22)
print("Nome: {}, Idade: {}".format(Pessoa1.nome, Pessoa1.idade))