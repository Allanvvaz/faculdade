lista_nomes = ["Ana", "Bruno", "Amanda", "Bia", "Carlos","allan", "cecilia", "davi"]
nomes_agrupados = {}
for nome in lista_nomes:
    primeira_letra = nome[0].upper() 

    if primeira_letra not in nomes_agrupados:
        nomes_agrupados[primeira_letra] = []

    nomes_agrupados[primeira_letra].append(nome)
resultado_final = []

for nome_original in lista_nomes:
    primeira_letra = nome_original[0].upper()

    if primeira_letra in nomes_agrupados:
        resultado_final.append(tuple(nomes_agrupados[primeira_letra]))
        del nomes_agrupados[primeira_letra]
        
print(resultado_final)