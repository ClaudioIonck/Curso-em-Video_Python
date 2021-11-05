'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota de {}: ' .format(nome)))
n2 = float(input('Digite a segunda nota de {}: ' .format(nome)))

media = (n1 + n2) / 2

print('A media das notas de {}, foi: {:.2f}' .format(nome, media))
