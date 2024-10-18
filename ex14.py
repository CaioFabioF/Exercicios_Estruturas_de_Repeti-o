f = 0
while True :
    n = int(input('Digite um número: '))
    f = n
    if f > 0 and f < 16 :
        for c in range(n-1,0,-1) :
            n = n * c
        print(n)
    if f < 0 or f > 16 :
        print('Valor inválido')
        break
print('Fim')