x = int(input('Escolha um número'))
d = x * 2
t = x * 3
r = d
if x % 2 == 0 and d == r:
    print(x,'é positivo e seu dobro é:',d)
else:
    print(x,'é negativo e seu triplo é',t)
