lista= []
lista2= []
for i in range(1, 7):
    lista.append(float(input(f"Coloque uma nota: ")))

print("Todas notas: ", lista)

for i in range(len(lista)):
    if lista[i] >= 7:
        lista2.append(lista[i])
print("Notas aprovadas: ", lista2)
print("Média das notas aprovadas: ", sum(lista2)/len(lista2))

