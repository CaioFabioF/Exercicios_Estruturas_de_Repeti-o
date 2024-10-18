s = 0
q = 0
while True :
    n = int(input('Digite a sua idade: '))
    if n < 0 :
        break
    s += n
    q += 1
m = s / q
if m > 0 and m < 26 :
    print(f'A turma é jovem, a médiade idade foi {m}')
elif m > 26 and m < 60 :
    print(f'A turma é adulta, a média de idade foi {m}')
elif m > 60 :
    print(f'A turma é idosa, a média de idade foi {m}')

