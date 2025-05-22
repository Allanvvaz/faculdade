lista = ["casa", "achar", "carro", "carta"]
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
              'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
listaCorreta = []
for i in lista:
    alterna = True
    for j in range(len(i) - 1):
        atual = i[j].lower()
        proxima = i[j + 1].lower()
        if (atual in vogais and proxima in vogais) or (atual in consoantes and proxima in consoantes):
            alterna = False
            break
    if alterna:
        listaCorreta.append(i)
print(listaCorreta)
