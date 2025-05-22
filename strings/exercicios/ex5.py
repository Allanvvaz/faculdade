entrada = ["Organização Mundial da Saúde", "Banco Central"]
entrada = [x.split() for x in entrada]
siglas = []
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in entrada:
    sigla = ""
    for j in i:
        if j[0] in alfabeto:
            sigla += j[0]
    siglas.append(sigla)
    
print(siglas)
       




