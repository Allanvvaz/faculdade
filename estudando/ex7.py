#Exercicio 7 - Separando Dígitos de um Número
# Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos dígitos separados.
numero = int(input("Digite um número menor que 1000: "))
centena = numero // 100
dezena = (numero // 10) % 10
unidade = numero % 10

print(f"{centena} centenas, {dezena} dezenas e {unidade} unidades")