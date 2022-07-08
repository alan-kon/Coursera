seguidores ="""colar aqui"""
#definir novos no shell
import re
def qmehofdp():
    fdp=[]
    novosl=[]
    seguidoresl=[]
    for item in re.findall("[A-Za-z]{4}\s[a-z]{2}\s[a-z]{6}\s[a-z]{2}\s[a-z0-9._]+", novos):
        novosl.append(item)
    for item in re.findall("[A-Za-z]{4}\s[a-z]{2}\s[a-z]{6}\s[a-z]{2}\s[a-z0-9._]+", seguidores):
        seguidoresl.append(item)
        if item not in novosl:
            fdp.append(item)
            print (item[18:])
    print (len(fdp))
    print(len(seguidoresl))
    print(len(novosl))
    
