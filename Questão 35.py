prod = float(input('Valor do produto: '))
d = prod - ( 10 / 100)
cc = prod - ( 15 / 100 )
x2 = prod
x3 = prod + (10/100)
if d <= cc and d <= x3:
    print('Compre com dinheiro.')
elif cc <= x3:
    print('Compre com cartão de crédito.')
else:
    print('Compre em 2x mais 10% de juros')