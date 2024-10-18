termo1 = 0
termo2 = 1
n = int(input('Digite até que termo deseja ver a série de Fibonacci: '))
for c in range(0,n) :
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    print(termo3)