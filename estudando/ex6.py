#Exercicio 6 - Validação de Data
# Faça um programa que leia uma data (dia, mês e ano) e verifique se a data é válida.
data = input("Digite uma data (dd/mm/aaaa): ")
dia, mes, ano = map(int, data.split("/"))
meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    meses[1] = 29
if 1 <= mes <= 12 and 1 <= dia <= meses[mes - 1]:
    print("Data válida")
else:
    print("Data inválida")