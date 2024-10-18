pp = float(input('Digite o preço do pão: '))
print(f'O preço do pão é {pp}.')
print('Panificadora Ei cortinas vai tomar no c*')
for c in range(1,51) :
    print(f'{c} - R$ {c*pp:.2f}.')