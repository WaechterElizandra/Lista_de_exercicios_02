peso = float(input('Informe peso (kg): '))
altura = float(input('Informe a altura (m) : '))
imc = float(peso / altura ** 2)
if imc < 18.5:
    print('CUIDADO!!! Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('PARABÉNS!!! Seu peso está normal')
elif 25 <= imc < 30:
    print('CUIDADO!!!!Você está acima do peso')
elif imc > 30:
    print('ATEÇÃO!!!Você está muito acima do peso')
