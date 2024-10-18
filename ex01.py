n = 0
while True :
    n = int(input('Digite um número: '))
    if n > 0 and n < 10 :
        print('Valor Válido')
        break
    print('Valor inválido')