def soma_hipotenusas(n):
    soma=0
    x=1
    while x<=n:
        if é_hipotenusa(x):
            soma=soma+x

        x=x+1
    return soma

def é_hipotenusa(x):
    j=1
    while j<x:
        c=1
        while c<x:
            if x**2==j**2+c**2:
                return True
            c=c+1
        j=j+1

    return False
