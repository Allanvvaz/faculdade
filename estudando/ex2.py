#Exercicio 2 - Turno
# Faça um programa que leia o turno de um aluno e mostre uma saudação.
turno = input("Qual turno você estuda? M (matutino), V (Vespertino) ou N (Noturno): ")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("valor inválido!")