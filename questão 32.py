altura = float(input('Digite sua altura: '))
sexo = input('Digite o seu sexo (F/M): ')
if (sexo == 'M'):
    peso_homem = 72.7 * altura - 58
    print('O seu peso ideal é: ', peso_homem, 'Kg')
else:
    peso_mulher = int(62.1 * altura - 44.7)
    print('O seu peso ideal é: ', peso_mulher, 'Kg')
