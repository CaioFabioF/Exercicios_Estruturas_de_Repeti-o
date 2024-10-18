n = int(input('Digite até que termo deseja ver: '))
f = 1
soma = 0
for c in range(1,n+1,+2) :
    s = f / c
    print(f'{f} / {c}')
    soma += f / c
    f += 1
print(f'A soma dos valores divididos é {soma}')
