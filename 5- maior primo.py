def maior_primo(n):
    while n!=0:
        i=2
        primo=True
        while i<n:
            if n%i==0:
                primo=False
            i=i+1
        if primo:
            return n
            n=0
        else:
            n=n-1
    

