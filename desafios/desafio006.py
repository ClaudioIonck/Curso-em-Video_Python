'''
Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
'''

n = int(input('Digite um numero: '))

d = n * 2
t = n * 3
r = n**(1/2) # raiz quadrada

# \n quebra linhas
print('Para esse numero {}, \nO seu dobro é {}, \nO seu triplo é {}, \nE sua raiz quadrada é {:.2f}' .format(n, d, t, r))
