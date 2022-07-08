def remove_repetidos(lista):
    lista2=sorted(lista)
    i=0
    x=len(lista2)
    while i+1<len(lista2):
        if lista2[i]==lista2[i+1]:
            del lista2[i]
        else:
            i=i+1
    return lista2
    
