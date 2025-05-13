x = int(input("Coloque um número: "))

if x < 0:
	valor_absoluto = x * -1
else:
	valor_absoluto = x
	
print(f"O valor absoluto de {x} é {valor_absoluto}.")