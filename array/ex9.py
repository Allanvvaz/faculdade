listaComprada = ["leite", "pão", "queijo"]
listaPopular = ["leite", "pão", "queijo", "manteiga", "presunto", "requeijão"]
diferencaLista = set(listaPopular) - set(listaComprada)
if all(x in listaComprada for x in listaPopular):
        print("Você comprou tudo o que estava na lista.")
else:
    print("Você não comprou tudo o que estava na lista, falta: ", diferencaLista)