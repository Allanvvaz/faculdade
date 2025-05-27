lista = []
while True:
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    dados = {}
    dados["nome"] = nome
    dados["quantidade"] = quantidade
    lista.append(dados)
    print(f"Produto: {dados['nome']}, Quantidade: {dados['quantidade']}")
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break
    

print(f"Nome dos produtos: {[produto['nome'] for produto in lista]}")
print(f"Quantidade dos produtos: {[produto['quantidade'] for produto in lista]}")