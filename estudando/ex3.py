# Exercicio 3 - Média e Conceito
# Faça um programa que leia duas notas de um aluno, calcule a média e mostre o conceito do aluno.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >=9 and media<= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media >= 0 and media < 4:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    print("Aprovado com conceito", conceito)
else:
    print("Reprovado com conceito", conceito)