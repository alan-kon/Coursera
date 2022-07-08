def menor_nome(nomes):
    nome=nomes[0].strip()
    for i in nomes:
        semesp=i.strip()
        if len(semesp)< len(nome):
            nome=semesp
    return nome.capitalize()
