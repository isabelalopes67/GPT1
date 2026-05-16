listaNotas = [] #Criamos uma lista vazia

print("-" * 40)
print("Bem vindo a I.A que calcula notas e média final 😂😊")

while True:
    notas = input("Digite a nota que deseja inserir (digite sair para parar): ")

    if notas.lower() == "sair": #comando LOWER obriga a entrada ser toda minuscula
         break 
    else:
         listaNotas.append(float(notas)) #Insere dados em uma lista

média = sum(listaNotas) / len(listaNotas)

print(f"A média final do aluno é {média:.2f}") #:.2f limita a saída

