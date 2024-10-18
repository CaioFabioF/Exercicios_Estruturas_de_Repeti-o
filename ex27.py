n = int(input('Digite um número: '))
for c in range(2,n+1):
    primo = True
    for i in range(2,int(n**0.5)+1) :
        if n % i == 0 :
            primo = False
            print('Não é primo')
            break
    if primo == True :
        print('É primo')
        break