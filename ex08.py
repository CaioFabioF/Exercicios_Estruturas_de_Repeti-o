a = int(input('Digite o primeiro termo: '))
b = int(input('Digite o segundo termo: '))
s = 0
for c in range(a,b+1) :
    s += c
    print(c)
print(s)