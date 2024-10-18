while True:
    nome = str(input('Digite o seu nome: '))
    if len(nome) <= 3 :
        print('Inválido')
        break
    if len(nome) > 3 :
        print('Válido')
    idade = float(input('Digite a sua idade: '))
    if idade < 0 or idade > 150 :
        print('Inválido')
        break
    if idade > 0 and idade < 150 :
        print('Válido')
    salario = float(input('Digite o seu salário: '))
    if salario > 0 :
        print('Válido')
    if salario < 0 :
        print('Inválido')
        break
    sexo = str(input('Digite o seu sexo[F/M]: ')).strip().upper()
    if sexo in 'FfMm' :
        print('Válido')
    if sexo not in 'FfMm':
        print('Inválido')
        break
    estcivil = str(input('C casado, S solteiro, V viuvo, D divorciado: ')).strip().upper()
    if estcivil in 'CcSsVvDd' :
        print('Válido')
    if estcivil not in 'CcSsVvDd' :
        print('Inválido')
        break
