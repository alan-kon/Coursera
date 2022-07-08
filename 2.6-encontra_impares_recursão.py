def encontra_impares(lista):
    base=True
    for i in range(0, len(lista)):
        if lista[i]%2==0:
            base=False
    if base:
        return lista
    else:
        if lista[0]%2==0:
            return encontra_impares(lista[1:])
        else:
            impar=[]
            impar.append(lista[0])
            lista.extend(impar)
            return encontra_impares(lista[1:])
