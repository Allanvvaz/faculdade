lista_total = []
lista_maiores = []
lista_menores = []
while True:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    if idade < 0:
        print("Idade não pode ser negativa. Tente novamente.")
        continue
    if idade >= 18:
        lista_maiores.append(nome)
    else:
        lista_menores.append(nome)
    lista_total.append((nome, idade))
    info_pessoas = {
        "Maiores": lista_maiores,
        "Menores": lista_menores
    }
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break
print(info_pessoas)
print(lista_total)


