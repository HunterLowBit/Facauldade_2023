class veiculo:
    def __init__(self, nome, cor, modelo, placa):
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.placa = placa
        
class carro(veiculo):
    def __init__(self, nome, cor, modelo, placa):
        super().__init__(nome, cor, modelo, placa)


     

        
c1 = carro('Uno','Azul','Fiat','ASD-1256')
c2 = carro('Onix','Cinza','Chevrolet','KNG-1376')
c3 = carro('Sandero','Bege','Renault','RJN-9154')
c4 = carro('Fusca','Preto','Volkswagen','PKG-3320')
c5 = carro('Logan','Amarelo','Renault','KKF-5132')
c6 = carro('HB20','Branco','Hyundai','PGA-5285')
c7 = carro('Fit','Vermelho','Honda','ASA-6684')
c8 = carro('Hilux','Rosa','Toyota','FAD-3020')
c9 = carro('A3','Laranja','Audi','PTS-2589')
c10 = carro('M3','Brasil','BMW','AHG-4584')

print(f"""      
            Primeiro Veiculo             
          Nome do veiculo: {c1.nome}    
          cor: {c1.cor}                
          Modelo: {c1.modelo}           
          Placa: {c1.placa}   
          
          
            Segundo Veiculo
          Nome do veiculo: {c2.nome}
          cor: {c2.cor}
          Modelo: {c2.modelo}
          Placa: {c2.placa}
          
          
            Terceiro Veiculo
          Nome do veiculo: {c3.nome}
          cor: {c3.cor}
          Modelo: {c3.modelo}
          Placa: {c3.placa}         
          
          
            Quarto Veiculo
          Nome do veiculo: {c4.nome}
          cor: {c4.cor}
          Modelo: {c4.modelo}
          Placa: {c4.placa}
          
          
            Quinto Veiculo
          Nome do veiculo: {c5.nome}
          cor: {c5.cor}
          Modelo: {c5.modelo}
          Placa: {c5.placa}
          
          
            Sexto Veiculo
          Nome do veiculo: {c5.nome}
          cor: {c5.cor}
          Modelo: {c5.modelo}
          Placa: {c5.placa}
          
          
            Sétimo Veiculo
          Nome do veiculo: {c7.nome}
          cor: {c7.cor}
          Modelo: {c7.modelo}
          Placa: {c7.placa}
          
          
            Oitavo Veiculo
          Nome do veiculo: {c8.nome}
          cor: {c8.cor}
          Modelo: {c8.modelo}
          Placa: {c8.placa}
          
          
            Nono Veiculo
          Nome do veiculo: {c9.nome}
          cor: {c9.cor}
          Modelo: {c9.modelo}
          Placa: {c9.placa}
          
          
            Decimo Veiculo
          Nome do veiculo: {c10.nome}
          cor: {c10.cor}
          Modelo: {c10.modelo}
          Placa: {c10.placa}
      """)
