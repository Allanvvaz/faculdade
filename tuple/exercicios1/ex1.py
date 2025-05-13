funcionarios = [] 
tuple = ()
while True:
    print("1. Cadastrar funcionario")
    print("2. Listar todos funcionários")
    print("3. Listar funcionario por cargo")
    print("4. Media salarial por cargo")
    print("5. Funcionario com maior salário")
    print("6. Aumentar salário por nome")
    print("7. Remover funcionario por nome")
    print("8. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do funcionario: ")
        cargo = input("Digite o cargo do funcionario: ")
        salario = float(input("Digite o salário do funcionario: "))
        funcionario = (nome, cargo, salario)
        funcionarios.append(funcionario)
        print(f"Funcionario {nome} cadastrado com sucesso!")
    elif opcao == 2:
        if len(funcionarios) == 0:
            print("Nenhum funcionario cadastrado.")
        else:
            print("Funcionários cadastrados:")
            for i, f in enumerate(funcionarios):
                print(f"{i + 1}. Nome: {f[0]}, Cargo: {f[1]}, Salário: {f[2]}")
    elif opcao == 3:
        if len(funcionarios) == 0:
            print("Nenhum funcionario cadastrado.")
        else:
            cargo = input("Digite o cargo que deseja listar: ")
            funcionarios_por_cargo = [f for f in funcionarios if f[1] == cargo]
            if len(funcionarios_por_cargo) == 0:
                print(f"Nenhum funcionario encontrado com o cargo {cargo}.")
            else:
                print(f"Funcionários com o cargo {cargo}:")
                for f in funcionarios_por_cargo:
                    print(f"Nome: {f[0]}, Salário: {f[2]}")
    elif opcao == 4:
        if len(funcionarios) == 0:
            print("Nenhum funcionario cadastrado.")
        else:
            cargo = input("Digite o cargo que deseja calcular a média salarial: ")
            funcionarios_por_cargo = [f for f in funcionarios if f[1] == cargo]
            if len(funcionarios_por_cargo) == 0:
                print(f"Nenhum funcionario encontrado com o cargo {cargo}.")
            else:
                media_salarial = sum(f[2] for f in funcionarios_por_cargo) / len(funcionarios_por_cargo)
                print(f"Média salarial do cargo {cargo}: {media_salarial}")
    elif opcao ==5:
        if len(funcionarios)== 0:
            print("nenhum funcionario cadastrado.")
        else:
            maior_salario = max(funcionarios, key=lambda f: f[2])
            print(f"Funcionario com maior salário: Nome: {maior_salario[0]}, Cargo: {maior_salario[1]}, Salário: {maior_salario[2]}")
    elif opcao == 6:
        if len(funcionarios) == 0:
            print("Nenhum funcionario cadastrado.")
        else:
            nome = input("Digite o nome do funcionario que deseja aumentar o salário: ")
            aumento = float(input("Digite o valor do aumento em porcentagem(Sem o %): "))
            for f in funcionarios:
                if f[0] == nome:
                    novo_salario = f[2] + (f[2] * aumento / 100)
                    funcionarios[funcionarios.index(f)] = (f[0], f[1], novo_salario)
                    print(f"Salário do funcionario {nome} aumentado para {novo_salario}.")
                    break
            else:
                print(f"Funcionario {nome} não encontrado.")
    elif opcao == 7:
        if len(funcionarios) == 0:
            print("Nenhum funcionario cadastrado.")
        else:
            nome = input("Digite o nome do funcionario que deseja remover: ")
            for f in funcionarios:
                if f[0] == nome:
                    funcionarios.remove(f)
                    print(f"Funcionario {nome} removido com sucesso.")
                    break
            else:
                print(f"Funcionario {nome} não encontrado.")
    elif opcao == 8:
        print("Saindo")
        break
    else:
        print("Opção inválida. Tente novamente.")
    
print(funcionarios)
