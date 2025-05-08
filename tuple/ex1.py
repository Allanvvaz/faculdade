notas = []
while True:
    nota = int(input("1. Adicionar nota\n2. Listar notas\n3. Média das Notas\n4. Maior e Menor Nota\n5. Notas acima da Média\n6.Buscar Nota Especídifca\n7.Remover Nota\n8.Sair\nEscolha uma opção: "))
    if nota == 1:
        nota = float(input("Digite a nota: "))
        if nota < 0 or nota > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")               
        notas.append(nota)
    elif nota == 2:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")
        else:
            print("Notas cadastradas:")
            for i, n in enumerate(notas):
                print(f"{i + 1}. {n}")
    elif nota == 3:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")
        else:
            media = sum(notas) / len(notas)
            print(f"Média das notas: {media}")
    elif nota == 4:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")
        else:
            maior_nota = max(notas)
            menor_nota = min(notas)
            print(f"Maior nota: {maior_nota}")
            print(f"Menor nota: {menor_nota}")
    elif nota == 5:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")
        else:
            media = 7
            notas_acima_media = [n for n in notas if n >= media]
            if len(notas_acima_media) == 0:
                print("Nenhuma nota acima da média.")
            else:
                print("Notas acima da média:")
                for n in notas_acima_media:
                    print(n)
    elif nota == 6:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")
        else:
            busca = float(input("Digite a nota que deseja buscar: "))
            if busca in notas:
                print(f"A nota {busca} está cadastrada na posição {notas.index(busca) + 1}.")
            else:
                print(f"A nota {busca} não está cadastrada.")
    elif nota == 7:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")
        else:
            busca = float(input("Digite a nota que deseja remover: "))
            if busca in notas:
                notas.remove(busca)
                print(f"A nota {busca} foi removida.")
            else:
                print(f"A nota {busca} não está cadastrada.")
    elif nota == 8:
        print("Saindo")
        break
    else:
        print("Opção invalida. Tente novamente.")
    

    Tuple = tuple(notas)

    for i in range(len(Tuple)):
        print(f"Nota {i+1}: {Tuple[i]}")
