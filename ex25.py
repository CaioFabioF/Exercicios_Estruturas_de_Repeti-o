q = 0
s = 0
lista = []
while True :
    t = int(input('Digite a temperatura em Kelvin: '))
    s += t
    q += 1
    lista.append(t)
    c = str(input('Deseja continuar[S/N]: ')).strip().upper()
    if c in 'Nn':
        break
m = s / q
print(f'A temperatura mais baixa foi {min(lista)} K, a mais alta foi {max(lista)} K. E a média de temperatura foi {m} K.')