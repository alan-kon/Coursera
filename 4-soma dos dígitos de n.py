n=input("Digite um número inteiro: ")
nn=int(n)
i=1
soma=0
while len(n)>=i:
    soma=soma+nn%10
    i=i+1
    nn=nn//10
print(soma)
