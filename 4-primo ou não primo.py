n=int(input("Digite um número inteiro: "))
while n!=0:
    i=2
    primo=True
    while i<n:
        if n%i==0:
            primo=False
        i=i+1
    if primo==True:
        print("primo")
    else:
        print("não primo")
    n=int(input("Digite um número inteiro: "))
