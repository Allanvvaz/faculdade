entrada = "hoje o dia está bonito e o dia está claro"
fraseLower = entrada.lower() 
palavras_na_frase = fraseLower.split(" ") 

palavras_iguais = [] 
frase_mudada = []      

for i in palavras_na_frase:
    if i in palavras_iguais:
        frase_mudada.append(f"{i}*")
    else:
        frase_mudada.append(i)
        palavras_iguais.append(i)

saida_final = " ".join(frase_mudada)

print(saida_final)