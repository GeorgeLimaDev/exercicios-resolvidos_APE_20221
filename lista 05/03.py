#Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0 (zero).

import random
tamanho = int(input('Tamanho da matriz quadrada: '))
matrizA = [[None] * tamanho for i in range (tamanho)]

for i in range (tamanho):
    for j in range (tamanho):
        matrizA[i][j] = random.randint(0, 20)

print('Matriz A:')
for i in range (tamanho):
    for j in range (tamanho):
        print(f'{matrizA[i][j]:4}',end=' ')
    print('')

matrizB = [[None] * tamanho for i in range (tamanho)]
for i in range (tamanho):
    for j in range (tamanho):
        matrizB[i][j] = matrizA[i+(i)][j+(j)]

print('Matriz B:')
for i in range (tamanho):
    for j in range (tamanho):
        print(f'{matrizB[i][j]:4}',end=' ')
    print('')

#incompleta e com um erro na atribuição dos valores de B.