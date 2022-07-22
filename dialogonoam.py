def dialogo():
    x=input('Boa Noite, aqui é o madrich Dans. Preciso de ajuda. Com que kvutzot estou falando? ')
    if x.lower() == 'machar' or x.lower() == 'shemesh' or x.lower() == 'shemesh e machar' or x.lower() == 'machar e shemesh':
        print(f'{x}, que bom que estou falando com vocês! Consegui hackear um computador deles para me comunicar secretamente.')
        print('Tentei salvar meus amigos vindo até a base secreta dos sequestradores, o último lugar que me procurariam. Não posso revelar onde estou escondido pois é muito perigoso chegar até aqui ')
        z=input('Estou completamente desesperado. Eles já pegaram todos os madrichim, só eu sobrei. Vocês podem me ajudar? ')
        if z.lower() == 'sim' or z.lower()== 's' or z.lower()=='sim!' or z.lower()=='claro':
            y=input('Muito obrigado! Preciso que vocês digitem um código para mim. Posso enviá-lo? ')
            if y.lower() == 'sim' or y.lower()== 's' or y.lower()=='sim!' or y.lower()=='claro':
                print("""
               _
              (_)          _
          _         .=.   (_)
         (_)   _   //(`)_
              //`\/ |\ 0`\\
              ||-.\_|_/.-||
              )/ |_____| \(    _
             0   |/\ /\|  0   (_)
                _| o o |_
         _     ((|, ^ ,|))
        (_)     `||\_/||`
                 || _ ||      _
                 | \_/ |     (_)
             0.__.\   /.__.0
              `._  `"`  _.'
                 / ;  \ \


                 
 ▄▄▄██▀▀▀▒█████   ██ ▄█▀▓█████  ██▀███  
   ▒██  ▒██▒  ██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
   ░██  ▒██░  ██▒▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██▄██▓ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
 ▓███▒  ░ ████▓▒░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▓▒▒░  ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░    ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░ ░  ░ ░ ░ ▒  ░ ░░ ░    ░     ░░   ░ 
 ░   ░      ░ ░  ░  ░      ░  ░   ░

 O CÓDIGO É: start video.mp4 """)
            else:
                print('não entendi, repita sua última resposta de maneira diferente')
                dialogo()
        else:
            print('não entendi, repita sua última resposta de maneira diferente')
            dialogo()
    else:
        print('não entendi, repita sua última resposta de maneira diferente')
        dialogo()

dialogo()


