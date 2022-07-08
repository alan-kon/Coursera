decrescente=True
anterior=int(input("Digite o primeiro número: "))
valor=1
while valor !=0 and decrescente:
    valor=int(input("Digite o próximo número: "))
    if valor>anterior:
            decrescente=False
    anterior =valor
if decrescente:
    print("A sequência é decrescente")
else:
    print("A sequência não é decrescente")
