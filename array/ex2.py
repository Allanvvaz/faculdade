lista = [0,1,2,3,4,5,6,7,8,9,10]
newLista = []
for i in range(len(lista)):
    if lista[i] % 2 == 0 and lista[i] != 0:
        newLista.append(lista[i] * lista[i])
    
print(newLista)   