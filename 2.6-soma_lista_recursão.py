def soma_lista(lista):
    tamanho=len(lista)
    if tamanho==1:
        return lista[0]
    else:
        lista[tamanho-2]=lista[tamanho-2]+lista[tamanho-1]
        return soma_lista(lista[0:tamanho-1])
