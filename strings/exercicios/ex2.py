array = ["pé", "de", "péde", "bola", "futebol", "fute", "bol","ba","la","bala"]
arrayJuntos = []
for i in range(len(array)):
    for j in range(len(array)):
        if i != j:
            palavra_combinada = array[i] + array[j]
            if palavra_combinada in array:
                arrayJuntos.append(palavra_combinada)
    
print(arrayJuntos)

