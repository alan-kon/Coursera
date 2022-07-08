n=input("Digite um número inteiro: ")
nn=int(n)
if nn==0:
    print("não")
else:
    i=1
    adjacente=False
    while len(n)>=i:
        y=nn%10
        x=(nn//10)%10
        if y==x:
            adjacente=True
        i=i+1
        nn=nn//10

    if adjacente:
        print("sim")
    else:
        print("não")
