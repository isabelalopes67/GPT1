print("Bem vindo ao portal Educacional do Platini")

notaUm = float(input("Digite a primeira nota do aluno: "))
notaDois = float(input("Digite a segunda nota do aluno: "))
notaTres = float(input("Digite a terceira nota do aluno: "))
notaQuatro = float(input("Digite a quarta nota do aluno: "))

média = (notaUm + notaDois + notaTres + notaQuatro) / 4

print(f"A média é {média}")

if média >= 6:
    print("Parabéns! Você está aprovado!")
else:
    print("você está reprovado! Estude mais no ano que vem!") 
