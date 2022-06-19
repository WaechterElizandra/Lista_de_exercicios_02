n = int(input("Quantos números: "))
n1 = 0
n2 = 0
n3 = 0
n4 = 0
i = 0
num = int(input('Digite um número'))
while i > 0:
    i = i + 1
    if num > 0 and n <= 25:
        n1 = n1 +1
    elif num >= 26 and n <= 50:
         n2 = n2 + 1
    elif num >= 51 and n <= 75:
         n3 = n3 + 1
    else:
         n4 = n4 +1
print ('Primeiro intervalo',n1)
print ('Segundo intervalo',n2)
print ('Terceiro intervalo',n3)
print ('Quarto intervalo',n4)