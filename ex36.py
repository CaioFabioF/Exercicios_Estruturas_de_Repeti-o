n = int(input('Informe até que termo deseja ver: '))
m = 1
s = 0
for c in range(1,n+1) :
    print(f'{c} / {m}')
    s += c/m
    m += 2
print(f'A média de todos os valores dividos é {m}')