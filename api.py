#Instalar bibliotecas 
#pip install requests

#Segundo passo: adicionar/importar ao código 
import requests 

nome = input("digite o seu nome: ")
email = input("digite o seu e-mail: ")
telefone = input("digite seu telefone: ")
#colhe o cep
cep = input("Qual seu cep?")

#cria uma vaeiavel e atribuiu o resultado do link
#utilizamos o f string, para conseguir inserir uma variavel 
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url).json()

print(f"Bem vindo ao Mercado Livre {nome}! o seu e-mail é {email}. O seu telefone é {telefone}. Você mora na rua {dados['logradouro']}, na cidade {dados['localidade']}, no estado de {dados['estado']}.") 

#atribuindo variaveis para cada um dos resultados
# rua = dados['logradouro']
# bairro = dados['bairro']
# cidade = dados['localidade']


# print(rua)
# print(bairro)
# print(cidade)

