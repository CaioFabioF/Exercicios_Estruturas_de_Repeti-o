numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    divisores = []
    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)
    
    if divisores:
        print(f"{numero} não é um número primo. Ele é divisível por: {divisores}")
    else:
        print(f"{numero} é um número primo.")
