n = int(input('Digite um número: '))
num = 1
contador = 0
while num < n:
    if num % 2 == 0:
        contador = contador + 1
    num = num + 1
print(contador)