pesos = []
alturas = []
q = 0
a = 0
p = 0
while True:
    peso = int(input('Digite o seu peso: '))
    p += peso
    altura = int(input('Digite a sua altura em cm : '))
    a += altura
    q +=1
    pesos.append(peso)
    alturas.append(altura)
    c = str(input('Deseja continuar[S/N]? '))

    if c in 'Nn':
        break
    m1 = p / q
    m2 = a / q
print(f'O mais magro é {min(pesos)}, e o mais gordo é {max(pesos)}.')
print(f'O mais baixo é {min(alturas)}, e o mais alto é {max(alturas)}.')
print(f'A média de pesos é {m1} e a média de altura é {m2}.')
