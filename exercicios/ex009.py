'''
Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
'''
num = int(input('Digite o numero para gerar a tabuada: '))
num2 = int(input('Até qual numero a tabuada deve ir? '))
for t in range(1, num2+1):
    print(f'{num} X {t} = {num * t}')
    print()
