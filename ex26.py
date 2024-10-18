# Solicita ao usuário um número inteiro
limite = int(input("Digite um número inteiro: "))

# Lista para armazenar os números primos
primos = []

# Verifica cada número de 2 até o limite
for numero in range(2, limite + 1):
    # Verifica se o número é primo
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    # Adiciona o número à lista de primos se for primo
    if eh_primo:
        primos.append(numero)

# Exibe a lista de números primos
print(f"Números primos entre 1 e {limite}: {primos}")
