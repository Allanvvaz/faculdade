x = float(input("Coloque o primeiro número: "))
y = float(input("Coloque o segundo número: "))

if x < 0:
	valor_absolutoX = x * -1
else:
	valor_absolutoX = x
	
if x < 0:
	valor_absolutoY = y* -1
else:
	valor_absolutoY = y
	
if (valor_absolutoX - valor_absolutoY) < 3:
	print(True)
else:
    print(False)
