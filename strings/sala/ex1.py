palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite a segunda palavra para comparar: ")

palavra_lower1 = palavra1.lower()
palavra_lower2 = palavra2.lower()
if palavra_lower1 == palavra_lower2:
    print("Palavras iguais")
else:
    print("Palavras diferentes")

