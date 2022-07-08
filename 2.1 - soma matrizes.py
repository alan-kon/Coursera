def soma_matrizes(m1, m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        soma=[]
        n=0
        for i in m1:
            matriz=[]
            m=0
            for j in i:
                x=j+m2[n][m]
                matriz.append(x)
                m=m+1
            soma.append(matriz)
            n=n+1
        return soma
    else:
        return False

