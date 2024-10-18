qvei = 0
qaci = 0
qc2 = 0
cod1 = 0
cod2 = 0
aci1 = 0
aci2 = 0
for c in range(0,5) :
    cod = int(input('Digite o código da cidade: '))
    v = int(input('Digite a quantidade de veículos de passeio: '))
    aci = int(input('Digite a quantidade de acidentes: '))
    qvei += v
    if aci > aci1 :
        aci1 = aci
        cod1 = cod
    if aci < aci1 :
        aci2 = aci
        cod2 = cod
    medv = qvei / 5
    if v < 2000 :
        qaci += aci
        qc2 += 1
        meda = qaci/qc2

print(f'A média de veículos na 5 cidades são {medv}')
print(f'A média de acidentes de trânsitos nas cidades com menos de 2.000 habitantes são {meda}')
print(f'A cidade com mais acidentes é a {cod1} com {aci1}, a cidade com menos acidentes é {cod2} com {aci2} acidentes.')

