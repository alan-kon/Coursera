def maior_elemento(lista):
    i=0
    maior=lista[0]
    while i+1<len(lista):
        if lista[i]>lista[i+1] and lista[i]>maior:
            maior=lista[i]
            
        i=i+1
    if i+1==len(lista) and lista[i]>maior:
        maior=lista[i]
    return maior
