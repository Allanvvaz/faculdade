entrada = "vida longa ao rei"
palavras_processadas = [] 
lista_de_palavras = entrada.split()

for palavra in lista_de_palavras:
    if len(palavra) % 2 == 0: 
        palavra_invertida = palavra[::-1] 
        palavras_processadas.append(palavra_invertida)
    else:
        palavras_processadas.append(palavra) 
saida = " ".join(palavras_processadas)

print(saida)