estoque = {} 

while True:
    print("\n Estoque")
    menu = input("Digite:\n 1. Para adicionar/atualizar produtos\n 2. Para remover produtos\n 3. Para visualizar estoque\n 4. Sair\nEscolha uma opção: ")
    if menu == "1":
        produto = input("Digite o nome do produto: ")
        while True:
                quantidade = int(input(f"Digite a quantidade de {produto}: "))
                if quantidade < 0:
                    print("Quantidade não pode ser negativa. Tente novamente.")
                else:
                    break
        estoque[produto] = quantidade
        print(f"Produto '{produto}' adicionado/atualizado com quantidade {quantidade}.")
    elif menu == "2":
        produto = input("Digite o nome do produto a ser removido: ")
        if produto in estoque:
            del estoque[produto]
            print(f"Produto '{produto}' removido do estoque.")
        else:
            print(f"Produto '{produto}' não encontrado no estoque.")
    elif menu == "3":
        if not estoque:
            print("O estoque está vazio.")
        else:
            print("\n--- Estoque Atual ---")
            for produto, quantidade in estoque.items():
                print(f"- {produto}: {quantidade}")
    elif menu == "4":
        print("Saindo do sistema de estoque. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida do menu.")