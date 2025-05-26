entrada = """01/01/2025 Pix para Joãozinho -50,00
02/01/2025 Pix para Mariazinha -30,00
03/01/2025 Recebimento de salário 1.000,00
03/01/2025 Gasolina -200,00
04/01/2025 Hambúrguer sebosão -40,00"""

linhas = entrada.split("\n")

SaldoTotal = 0  

for linha in linhas:
    caracteres = linha.split(" ")
    data = caracteres[0]
    descricao = " ".join(caracteres[1:-1])
    valor_str = caracteres[-1].replace(".", "").replace(",", ".")
    
    valor = float(valor_str)
    SaldoTotal += valor  
    print(f"Data: {data}")
    print(f"Descrição: {descricao}")
    print(f"Valor: {valor:.2f}")

print(f"\n Saldo Total: R$ {SaldoTotal}")
