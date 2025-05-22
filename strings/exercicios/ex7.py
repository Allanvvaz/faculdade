lista = ["hello", "world", "123", "456", "python3", "abc123xyz", "789", "data", "science", "AI", "1", "2"]
listaLetra = []
listaNumero = []
listaAlfanumericas = []

for i in lista:
    if i.isalpha():
        listaLetra.append(i)
    elif i.isdigit():
        listaNumero.append(i)
    elif i.isalnum():
        listaAlfanumericas.append(i)

print(listaLetra)
print(listaNumero)
print(listaAlfanumericas)