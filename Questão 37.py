num_aluno = input('Informe o número do aluno')
nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))
me = ((nota1+nota2+nota3)/3)
ma = ((nota1+(nota2 * 2) + (nota3*3)+me)/7)
if ma >= 9.0:
    print('Estudante',num_aluno,'Aprovado com conceito A')
elif 7.5 <= ma < 9.0:
    print('Estudante',num_aluno,'Aprovado com conceito B')
elif 6.0 <= ma < 7.5:
    print('Estudante',num_aluno,'Aprovado com conceito C')
elif 4.0 <= ma < 6.0:
    print('Estudante',num_aluno,'Reprovado com conceito D')
elif ma < 4.0:
    print('Estudante',num_aluno,'Reprovado com conceito E')
