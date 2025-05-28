texto = input("Digite um texto: ")
letras = ["abcdefghijklmnopqrstuvwxyz"]
contagem = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
for letra in texto.lower():
    if letra in letras[0]:
        contagem[letra] += 1
print("contagem de letras:")
for letra, quantidade in contagem.items():
    if quantidade > 0:
        print(f"{letra}: {quantidade}")
