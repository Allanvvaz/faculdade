lista = []
listaCorreta = []

while True:
    cpf = input("Adicione um cpf(000.000.000-00) (ou digite 'sair' para encerrar): ")
    if cpf.lower() == "sair":
        break
    elif cpf.isdigit() and len(cpf) == 11:
        if cpf in lista:
            print("CPF já adicionado.")
            continue
        else:
            listaCorreta.append(cpf)
        continue
    lista.append(cpf)

print(listaCorreta)

#Adicionar a verificação de cpf
