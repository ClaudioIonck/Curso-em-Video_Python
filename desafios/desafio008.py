'''
Escreva um programa que leia um valor em metros e o exiba convertido em
centimetros e milimetros.
'''

medida = float(input('Digite o valor em metros: '))

cm = medida * 100
mm = medida * 1000
m = medida
km = medida / 1000
pl = medida * 39.3701     #polegadas in
pes = medida * 3.28084    #pés ft
yd = medida * 1.0936      #jardas yd
NM = medida * 0.00054     #milhas náuticas NM
mi = medida* 0.000621    #milha terrestre mi

print('A medida de {}m corresponde a: \n{:.0f} cm \n{:.0f} mm \n{} m \n{} km \n{:.0f} Polegadas \n{:.0f} Pés \n{:.1f} Jardas \n{} Milhas Náuticas \n{} Milhas Terrestres' .format(medida, cm, mm, m, km, pl, pes, yd, NM, mi))

