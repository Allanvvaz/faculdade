lista = []
for i in range(1, 5):
    lista.append(float(input(f"Coloque um número: ")))

lista.sort()

print("Segundo maior número: ",lista[-2])