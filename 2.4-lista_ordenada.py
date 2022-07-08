def ordenada(lista):
    for i in range(len(lista)-1):
        menor=lista[i]
        for j in range(i+1, len(lista)-1):
            if lista[j]<menor:
                return False
    return True
