# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="seu_banco_de_dados"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("create database Loja")

mycursor.execute("SELECT * FROM estoque")

for x in mycursor:
  print(x)


#mycursor.execute("CREATE TABLE estoque (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), descricao VARCHAR(255), quantidade INT)")
