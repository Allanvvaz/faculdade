
x = float(input("Coloque o primeiro número: "))
y = float(input("Coloque o segundo número: "))

maior_numero = x

if y > maior_numero:
    maior_numero = y

if maior_numero > 0:
    print(f"O maior número é {maior_numero} e é positivo.")
else:
    print(f"O maior número é {maior_numero} e é negativo.")