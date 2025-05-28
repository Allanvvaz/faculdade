frases = ["Eu gosto de Python", "Python é fácil", "Amo programação"]
palavra_chave = input("Digite uma palavra-chave: ").lower()
frases_filtradas = []
saida = []
for frase in frases:
    if palavra_chave in frase.lower():
        frases_filtradas.append(frase)
print("Frases filtradas:")
for frase in frases_filtradas:
    saida.append(frase.lower())
print(saida)
