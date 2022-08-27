#Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C). Ao final, exiba as 3 matrizes (no formato de matriz).

import random
linhas = 2
colunas = 3
matrizA = [[None] * colunas for i in range (linhas)]
matrizB = [[None] * colunas for i in range (linhas)]

for i in range (linhas):
    for j in range (colunas):
        matrizA[i][j] = random.randint(0,20)

for i in range (linhas):
    for j in range (colunas):
        matrizB[i][j] = random.randint(0,20)

print(f'Matriz A:')
for i in range (linhas):
    for j in range (colunas):
        print(f'{matrizA[i][j]:4}',end='')
    print('')

print(f'Matriz B:')
for i in range (linhas):
    for j in range (colunas):
        print(f'{matrizB[i][j]:4}',end='')
    print('')

matrizC = [[None] * colunas for i in range (linhas)]

for i in range (linhas):
    for j in range (colunas):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

print(f'Matriz C:')
for i in range (linhas):
    for j in range (colunas):
        print(f'{matrizC[i][j]:4}',end='')
    print('')