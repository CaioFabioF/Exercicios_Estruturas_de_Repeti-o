s = 0
q = 0
for c in range(1,6) :
    n = float(input('Digite um número: '))
    s += n
    q += 1
    m = s / q
print(f'A soma foi {s} e a média dos valores foi {m}')