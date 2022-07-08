print('Detecção de números primos')
n = int(input('Digite um número inteiro positivo:'))
i = 2
resultado = 0
while (i <= (n/2)):
    while ((n % i)==0):
        resultado = resultado + 1
        break
    i = i + 1
if (resultado == 0):
    print('O númeoo',n,'É um número primo.')
else:
    print('O númeoo', n, 'NÃO É um número primo.')
