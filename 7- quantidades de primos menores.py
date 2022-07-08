def n_primos(n):
    if n<2:
        return "número inválido"
    x=2
    soma=0
    while x<=n:
        nãoprimo=False
        i=2
        while i<x:
            if x%i==0:
                nãoprimo=True
            i=i+1
        if nãoprimo:
            soma=soma+1
        x=x+1
    return n-soma-1
