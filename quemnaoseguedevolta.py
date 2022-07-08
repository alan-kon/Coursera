seguindo="""copiar aqui"""

import re

def qmnao():
    seguindol=[]
    seguidoresl=[]
    naosdv=[]
    for item in re.findall("[A-Za-z]{4}\s[a-z]{2}\s[a-z]{6}\s[a-z]{2}\s[a-z0-9._]+", seguidores):
        seguidoresl.append(item)
    
    for item in re.findall("[A-Za-z]{4}\s[a-z]{2}\s[a-z]{6}\s[a-z]{2}\s[a-z0-9._]+", seguindo):
        seguindol.append(item)
        if item not in seguidoresl:
            naosdv.append(item)
            print (item[18:])
    print (len(naosdv))

def eunao():
    seguindol=[]
    seguidoresl=[]
    naosdv=[]
    for item in re.findall("[A-Za-z]{4}\s[a-z]{2}\s[a-z]{6}\s[a-z]{2}\s[a-z0-9._]+", seguindo):
        seguindol.append(item)
    
    for item in re.findall("[A-Za-z]{4}\s[a-z]{2}\s[a-z]{6}\s[a-z]{2}\s[a-z0-9._]+", seguidores):
        seguidoresl.append(item)
        if item not in seguindol:
            naosdv.append(item)
            print (item[18:])
    print (len(naosdv))
