produtos = []
while True:
    produto = int(input("1. Cadastrar Preço de Produto\n2. Listar Todos os Preços\n3. Valor Total em Estoque\n4. Preço Médio\n5. Produto mais Barato e Mais Caro\n6.COntar Preços Abaixo de X\n7.Remover Preço\n8.Sair\nEscolha uma opção: "))
    if produto == 1:
        produto = float(input("Digite o preço do produto: "))
        if produto < 0:
                print("Preço inválido. Digite um preço maior que 0.")               
        produtos.append(produto)
    elif produto == 2:
        if len(produtos) == 0:
            print("Nenhum preço cadastrado.")
        else:
            print("Preços cadastrados:")
            for i, p in enumerate(produtos):
                print(f"{i + 1}. {p}")
    elif produto == 3:
        if len(produtos) == 0:
            print("Nenhum preço cadastrado.")
        else:
            total = sum(produtos)
            print(f"Valor total em estoque: {total}")
    elif produto == 4:
        if len(produtos) == 0:
            print("Nenhum preço cadastrado.")
        else:
            media = sum(produtos) / len(produtos)
            print(f"Média dos preços: {media}")
    elif produto == 5:
        if len(produtos) == 0:
            print("Nenhum preço cadastrado.")
        else:
            maior_preco = max(produtos)
            menor_preco = min(produtos)
            print(f"Produto mais caro: {maior_preco}")
            print(f"Produto mais barato: {menor_preco}")
    elif produto == 6:
        if len(produtos) == 0:
            print("Nenhum preço cadastrado.")
        else:
            limite = float(input("Digite o valor limite: "))
            precos_abaixo_limite = [p for p in produtos if p < limite]
            if len(precos_abaixo_limite) == 0:
                print("Nenhum preço abaixo do limite.")
            else:
                print("Preços abaixo do limite:")
                for p in precos_abaixo_limite:
                    print(p)
    elif produto == 7:
        if len(produtos) == 0:
            print("Nenhum preço cadastrado.")
        else:
            busca = float(input("Digite o preço que deseja remover: "))
            if busca in produtos:
                produtos.remove(busca)
                print(f"O preço {busca} foi removido.")
            else:
                print(f"O preço {busca} não está cadastrado.")
    elif produto == 8:
                print("Saindo")
                break
    
    tupla = tuple(produtos)
    for i in range(len(tupla)):
        print(f"Produto {i + 1}: {tupla[i]}")
    
