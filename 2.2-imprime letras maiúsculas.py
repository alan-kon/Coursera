def maiusculas(frase):
    string=""
    for i in frase:
        if ord(i)>=65 and ord(i)<=90:
            string+=i
    return string
        
