n1 = 0
h1 = 0
h2 = 0
n2 = 0
for c in range(0,4) :
    n = int(input('Digite o seu número de aluno: '))
    h = int(input('Digite a sua altura em cm: '))
    if h > h1 :
        h1 = h
        n1 = n
    if h < h1 :
        h2 = h
        n2 = n
print(f'O aluno mais alto é o {n1} e sua altura é {h1}. O aluno mais baixo é o {n2} e sua altura é {h2}.')