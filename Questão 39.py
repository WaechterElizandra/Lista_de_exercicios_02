maior = 0
menor = 0
for pessoas in range(1,16):
    altura = float(input('Altura da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
print('Maior altura = ',maior)
print('Memor altura = ', menor)