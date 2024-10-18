n = int(input('Digite o número a ser tabuado: '))
c = int(input('Digite com que número começará: '))
f = int(input('Digite com qual número finalizará: '))
print(f'Montar a tabuada de {n}')
print(f'Começar por {c}')
print(f'Finalizar em {f}')
print('---'*30)
while True : 
    if f < c :
        print('O final é maior que o começo!')
        print('ERRO!!!')
        break
    for i in range(c,f+1) :
        print(f'{n} X {i} = {n*i}')
    break
print('---'*30)
print('Fim!')