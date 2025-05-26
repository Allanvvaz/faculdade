lista = []
while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    dados = {}
    dados["nome"] = nome
    dados["idade"] = idade
    lista.append(dados)
    print(f"Nome: {dados['nome']}, Idade: {dados['idade']}")
    if idade >= 18:
        print(f"é maior de idade? {True}")
    else:
        print(f"é maior de idade? {False}")
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print(lista)