palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
iguais = ""

for letra in palavra1:
    set(palavra1)

for letra in palavra2:
    if letra in palavra1:

        if letra not in iguais:
            iguais += letra

print("1ª" + palavra1)
print("2ª" + palavra2)
print("Letra iguais: " + iguais)