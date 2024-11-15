input = input()
input = input.split(" ")
dicionário = {}

for palavra in input:

    dicionário[palavra] = len(palavra)

print(dicionário)