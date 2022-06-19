a = int(input('Digite o valor inicial: '))
r = int(input('Digite o valor da razão: '))
pg = (10 == a * ( r ** a-1))
for c in range(a, pg + r, r):
    print(c)
