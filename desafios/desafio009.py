'''
Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
'''
num = int(input('Tabuada do número: '))
for n in range(11):
    print(f'{num} X {n} = {num * n}')
