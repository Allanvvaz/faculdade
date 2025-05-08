lista= [1,1,1,2,2,2,3,4,4,5,6,7,8,8,8,9,10]
newLista = []
for i in range(len(lista)):
    if lista[i] not in newLista:
        newLista.append(lista[i])

print(lista)
print(newLista)
                
                
        

