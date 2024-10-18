q1 = 0
q2 = 0
q3 = 0
q4 = 0
while True :
    n = int(input('Digite um número: '))
    if n < 0 :
        print('Número negativo!')
        break
    elif n > 0 and n <= 25 :
        q1 += 1
    elif n > 26 and n <= 50 :
        q2 += 1
    elif n > 51 and n <= 75 :
        q3 += 1
    elif n > 76 and n <= 100 :
        q4 += 1
    else :
        print('Número maior que 100')
print(f'São {q1} números entre 0 e 25')
print(f'São {q2} números entre 26 e 50')
print(f'São {q3} números entre 51 e 75')
print(f'São {q4} números entre 76 e 100')

