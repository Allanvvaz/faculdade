lista1 = [1,2,4,5,6,7,8,9]
lista2 = [11,22,34,56,78,77,88]
lista_intercalando= []
for i in range(len(lista1)):
    lista_intercalando.append(lista1[i])
    for j in range(len(lista2)):
        if i == j:
            lista_intercalando.append(lista2[j])

print(lista_intercalando)