n=L=int(input("digite a largura: "))
x=a=int(input("digite a altura: "))
while a>0:
    if a==x:
        while L>0:
            print("#", end="")
            L=L-1
    if a<x and a>1:
        L=2
        print("#", end="")
        while L>=2 and L<n:
            print(" ", end="")
            L=L+1
        print("#", end="")
        
    if a==1:
        L=n
        while L>0:
            print("#", end="")
            L=L-1       
    a=a-1
    print()
