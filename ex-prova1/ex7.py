x = int(input("Coloque um número: "))

x_impar = x % 2 != 0
x_multiplo5 = x % 5 == 0

if x_impar and x_multiplo5:
    print(f"{x} é ímpar e múltiplo de 5.")
else:
    print(f"{x} é ímpar e não é múltiplo de 5.")