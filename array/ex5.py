lista = [[1,2],[3,4],[5]]
lista_unica = []
for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista_unica.append(lista[i][j])
print(lista_unica)