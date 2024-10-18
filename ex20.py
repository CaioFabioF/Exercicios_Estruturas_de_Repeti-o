import random
c1 = 0
c2 = 0
c3 = 0
e = int(input('Digite a quantidade de eleitores: '))
for i in range(0,e) :
    v = int(input('Vote 1, 2 ou 3: '))
    if v == 1 :
        c1 += 1
    elif v == 2 :
        c2 += 1
    elif v == 3 :
        c3 += 1
    else :
        print('Candidato Inválido')
        break
print(f'O candidato A recebeu {c1} votos, o candidato B recebeu {c2} votos e o candidato C recebeu {c3} votos.')