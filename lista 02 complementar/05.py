#Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os seus coeficientes. Obs: se Δ for negativo, não existem as raízes da equação. Dica: use a função sqrt do módulo math.

import math


a = float(input('Termo A: '))
b = float(input('Termo B: '))
c = float(input('Termo C: '))
delta = (b * b) - (4 * a * c)

if delta < 0:
    print(f'Este resultado não geral raízes.')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print(f'Resultado X1: {x1}')
    print(f'Resultado X2: {x2}')