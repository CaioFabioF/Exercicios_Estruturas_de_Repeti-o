t = int(input('Digite até que termo irá a sequência: '))
l = []
s = 0
for c in range(0,t) :
    n = int(input('Digite um valor: '))
    if n > 0 and n < 1000 :
        s += n
        l.append(n)
print(f'A soma dos valores foi {s}, o menor valor foi {min(l)} e o maior valor foi {max(l)}.')
