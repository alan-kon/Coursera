import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(ass1, ass2):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e
deve devolver o grau de similaridade nas assinaturas.'''
    difs=0
    i=0
    while i<len(ass1):
        difs=difs+abs(ass1[i]-ass2[i])
        i+=1
    sab=difs/6
    return sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a
assinatura do texto.'''
    caracteres=0
    for sentenca in separa_sentencas(texto):
        separa_frases(sentenca)
        for frase in separa_frases(sentenca):
            separa_palavras(frase)
            for palavra in separa_palavras(frase):
                caracteres=caracteres + len(palavra)
    palavrastotal=[]
    for sentenca in separa_sentencas(texto):
        separa_frases(sentenca)
        for frase in separa_frases(sentenca):
            separa_palavras(frase)
            for palavra in separa_palavras(frase):
                palavrastotal.append(palavra)
    frasestotal=[]
    for sentenca in separa_sentencas(texto):
        separa_frases(sentenca)
        for frase in separa_frases(sentenca):
            frasestotal.append(frase)
    caracteressen=-1
    for sentenca in separa_sentencas(texto):
        separa_frases(sentenca)
        for palavra in separa_palavras(sentenca):
            caracteressen=caracteressen + len(palavra)+1
    caracteresfra=-1
    for sentenca in separa_sentencas(texto):
        separa_frases(sentenca)
        for frase in separa_frases(sentenca):
            separa_palavras(frase)
            for palavra in separa_palavras(frase):
                caracteresfra=caracteresfra + len(palavra)+1    
            
            
    wal2=caracteres/len(separa_palavras(texto))
    ttr2=n_palavras_diferentes(palavrastotal)/len(separa_palavras(texto))
    hlr2=n_palavras_unicas(palavrastotal)/len(separa_palavras(texto))
    sal2=caracteressen/len(separa_sentencas(texto))
    sac2=len(frasestotal)/len(separa_sentencas(texto))
    pal2=caracteresfra/len(frasestotal)
    return [wal2, ttr2, hlr2, sal2, sac2, pal2]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    sab=9999999999999
    i=0
    while i<len(textos):
        for texto in textos:
            asst=calcula_assinatura(texto)
            sabt=compara_assinatura(asst, ass_cp)
            if sabt<=sab:
                sab=sabt
                n=i
        i+=1
    return n
