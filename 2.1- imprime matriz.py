def imprime_matriz(matriz):
    for i in matriz:
        x=1
        for j in i:
            if x<len(i):
                print (j, "", end="")
            else:
                print (j)
            x=x+1
            

