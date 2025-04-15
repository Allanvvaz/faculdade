numero = int(input("Digite um número menor que 1000: "))
centena = numero // 100
dezena = (numero // 10) % 10
unidade = numero % 10

print(f"{centena} centenas, {dezena} dezenas e {unidade} unidades")