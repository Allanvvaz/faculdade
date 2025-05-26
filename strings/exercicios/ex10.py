Frase_1 = "A vida é bela"
Frase_2 = "a vida é dura mas bela"
lista_1 = Frase_1.split()
lista_2 = Frase_2.split()
lista_1 = [i.lower() for i in lista_1]  
lista_2 = [i.lower() for i in lista_2]  
palavras_iguais = []
for i in lista_1:
    if i in lista_2:
        palavras_iguais.append(i)

porcentagem = (len(lista_1) / len(lista_2)) * 100
print(porcentagem, "%")
print(palavras_iguais)