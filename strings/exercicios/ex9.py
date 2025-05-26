frase = "A A vida vida é é bela bela bela bela bela bela"
frase_split= frase.split()
frase_split = [i.lower() for i in frase_split]  
lista = []
palavras_unicas = []
palavras_repetidas = []
for i in frase_split:
    lista.append(i)

for i in lista:
    if i not in palavras_unicas:
        palavras_unicas.append(i)
    else:
        palavras_repetidas.append(i)
palavras_repetidas = list(set(palavras_repetidas))


print("Palavras repetidas:", palavras_repetidas)