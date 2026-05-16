print("-" *50)
print ("Bem vindo ao coletor de dados do Chat GPT 😊")
print ("-" * 50)

#declarações atuais
nome = input("Digite o seu nome: ")
email = input ("Digite o seu email: ") #variavel para armazenar email do usuario
cidade = input ("Digite a sua cidade")
Estado = input ("Digite o seu Estado")
País = input ("Digite o seu país")
nascimento = int(input("Digite o ano que você nasceu: "))
anoatual = int(input("Digite o ano que você esta: "))
idadeatual = anoatual - nascimento
#idadeAtual = int(input ("Digite a sua idade"))
#idadeFutura = idadeAtual + 1

#exibi as informacoes do usuario com mensagens personalizadas
print(f"Olá {nome}, a sua cidade é {cidade}, o seu estado é {Estado}, o seu país é {País}, a sua idade é {idadeatual}") #O f minusculo antes das aspas, permite que eu trabalhe com variaveis na frase. As chaves {} servem para eu chamar um variavel para dentro da frase

