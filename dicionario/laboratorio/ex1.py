lista = []
while True:
    aluno = input("Digite o nome do aluno : ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        print("Notas não podem ser negativas. Tente novamente.")
        continue
    if nota1 > 10 or nota2 > 10 or nota3 > 10:
        print("Notas não podem ser maiores que 10. Tente novamente.")
        continue
    media = (nota1 + nota2 + nota3) / 3
    aluno_info = {
        aluno: "Aprovado" if media >= 7 else "Reprovado",
    }
    tuple_notas = (nota1, nota2, nota3)
    tuple_info = (aluno, tuple_notas)
    print(aluno_info)
    lista.append(tuple_info)
    print(lista)
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break

