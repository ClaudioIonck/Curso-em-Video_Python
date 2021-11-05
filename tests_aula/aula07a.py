'''

nome = input('qual é seu nome? ')
print('prazer em te conhecer {:>20}!' .format(nome))
                             #alianhando a direita
print('prazer em te conhecer {:<20}!' .format(nome))
                             #alinhando a esquerda
print('prazer em te conhecer {:^20}!' .format(nome))
                             #alianhando ao centro
print('prazer em te conhecer {:=^20}!' .format(nome))
                             #desenhando formas entorno do nome
'''

n1 = int(input('de um valor:'))
n2 = int(input('de outro valor:'))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma vale {}, \n a subtração vale {}, a multiplicação vale {}, ' .format(s, sb, m,), end='')
print('a divisão vale {:.2f}, o pruduto vale {}, ao quadrado vale {:.2f}' .format( d, di, e))

#  \n serve para quedrar a linha
#  end="" serve para juntar os prints
