n = int(input('Digite quantas notas serão cadastradas: '))
nn = 0
q = 0
m = 0
for c in range(0,n) :
    notas = int(input('Digite uma nota: '))
    q += 1
    nn += notas
    m = nn / q
print(f'A média das notas foi {m}')
