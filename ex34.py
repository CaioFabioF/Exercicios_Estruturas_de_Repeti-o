q1 = q2 = q3 = q4 = qv = 0
qb = qn = 1
while True :
    print('''
    Votos:
    1 - Bolsonaro
    2 - Lula
    3 - G.Gómez
    4 - Flaco López
    5 - Branco
    6 - Nulo''')
    v = int(input('Digite o seu voto: '))
    qb = qn = 1
    if v == 0 or v > 6 :
        break
    elif v == 1 :
        q1 +=1
    elif v == 2 :
        q2 += 1
    elif v == 3 :
        q3 += 1
    elif v == 4 :
        q4 += 1
    elif v == 5 :
        qb += 1
    else :
        qn += 1
    qv += 1
    pvb = qv / qb
    pvn = qv / qn
print(f'''
Soma dos Votos :
Bolsonaro = {q1} votos
Lula = {q2} votos
G.Gomez = {q3} votos
Flaco López = {q4} votos
Brancos = {qb} votos, e sua porcentagem foi {pvb:.2f}%.      
Nulos = {qn} votos, e sua porcentagem foi {pvn:.2f}%.
No total foram {qv} votos.            
''')
