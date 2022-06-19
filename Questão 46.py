a = int(input('Digite o valor inicial: '))
r = int(input('Digite o valor da razão: '))
pa = a + (10 - 1) * r
for c in range(a, pa +  r, r):
    print(c)