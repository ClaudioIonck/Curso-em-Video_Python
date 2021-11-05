'''
Faça um programa que leia um numero inteiro e
mostre na tela o seu sucessor e seu antecessor.
'''

n = float(input('digite um numero: '))

suc = n + 1
ant = n - 1

print('O sucessor de {} é {}, e o antecessor é {}' .format(n, suc, ant))
