
def computador_escolhe_jogada(n, m):
    x=1
    while x!=m:
        if (n-x)%(m+1)==0:
            n=n-x
            print("O computador tirou", x, "peças.")
            print("Agora restam", n, "peças no tabuleiro.")
            print()
            return x
            x=m
        else:
            x=x+1
            if x==m:
                n=n-x
                print("O computador tirou", x, "peças.")
                print("Agora restam", n, "peças no tabuleiro.")
                print()
                return x
    if x==m:
            n=n-x
            print("O computador tirou", x, "peças.")
            print("Agora restam", n, "peças no tabuleiro.")
            print()
            return x
def usuario_escolhe_jogada(n, m):
    x=1
    while x<=m and x>0:
        x=int(input("Quantas peças você vai tirar?"))
        print()
        if x>m or x<=0:
            print("Oops! Jogada inválida! Tente de novo.")
            x=1
        else:
            n=n-x
            print("Você tirou", x, "peças.")
            print("Agora restam", n, "peças no tabuleiro.")
            print()
            return x
            x=0
    
        
        
def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    if n%(m+1)==0:
        print()
        print("Você começa!")
        print()
        while n>0:
            n=n-(usuario_escolhe_jogada(n, m))
            n=n-(computador_escolhe_jogada(n, m))
        print("Fim do jogo! O computador ganhou!")
    else:
        print()
        print("Computador começa!")
        print()
        while n>0:
            n=n-(computador_escolhe_jogada(n, m))
            if n>0:
                n=n-(usuario_escolhe_jogada(n, m))
        print()
        print("Fim do jogo! O computador ganhou!")
        print()
        
            
def campeonato():
    print("**** Rodada 1 ****")
    print()
    partida()
    print()
    print("**** Rodada 2 ****")
    print()
    partida()
    print()
    print("**** Rodada 3 ****")
    print()
    partida()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")
    
    
def início():
    x=0
    while x!=1 or x!=2:
        print("Bem-vindo ao jogo do NIM! Escolha: ")
        print()
        print("1 - para jogar uma partida isolada")
        x=int(input("2 - para jogar um campeonato "))
        if x==1:
            print()
            print("Voce escolheu uma partida!")
            print()
            partida()
        if x==2:
            print()
            print("Voce escolheu um campeonato!")
            print()
            campeonato()
            
        
início()
