p = 0
i = 0
for c in range(0,10) :
    n = int(input('Digite um número: '))
    if n % 2 == 0 :
        p += 1
    else :
        i += 1
print(f'A quantidade de números pares foi {p} e quantidade de números ímpares foi {i}')