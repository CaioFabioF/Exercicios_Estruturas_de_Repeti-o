n = int(input('Digite o número a iniciar o fatorial: '))
nn = n
print(f'O fatorial de {nn}:')
print(f'{nn}! :',end=' ')
for c in range(n-1,1,-1) :
    print(f'{n} . {c}',end=' ')
    n = n * c
print(f'={n}',end=' ')