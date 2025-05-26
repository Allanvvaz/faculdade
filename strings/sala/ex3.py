# Código errado
'''nomeCompleto = input("Digite seu nome completo: ")
nomeCompleto = nomeCompleto.lower()
nomeCompleto = nomeCompleto.split(" ")
primeiroNome = nomeCompleto[0]
ultimoNome = nomeCompleto[-1]

print(f"Primeiro nome: {primeiroNome}")
print(f"Último nome: {ultimoNome}")
vogais = "aeiou"

for letra in nomeCompleto:
    if letra in vogais:
        nomeCompleto.replace(letra, "*")
    
print(f"Nome completo com vogais substituídas por '*': {nomeCompleto}")'''


nome_completo = input("Digite seu nome completo: ")
nome_completo = nome_completo.lower()
partes = nome_completo.split(" ")
primeiro_nome = partes[0]
ultimo_nome  = partes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último  nome: {ultimo_nome}")

vogais = "aeiouAEIOU"
nome_sem_vogais = nome_completo
for v in vogais:
    nome_sem_vogais = nome_sem_vogais.replace(v, "*")

print(f"Nome completo com vogais substituídas por '*': {nome_sem_vogais}")
