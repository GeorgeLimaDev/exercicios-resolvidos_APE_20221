'''
Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma
dada matriz.
Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].
Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
duas matrizes (no formato de matriz).
'''

import random
linhas = 3
colunas = 5
original = [[None] * colunas for i in range (linhas)]
transposta = [[None] * linhas for i in range (colunas)]

for i in range (linhas):
    for j in range (colunas):
        original[i][j] = random.randint(1, 20)

for i in range (colunas):
    for j in range (linhas):
        transposta[i][j] = original[j][i]

print('Original: ')
for i in range (linhas):
    for j in range (colunas):
        print(f'{original[i][j]:4}',end=' ')
    print('')

print('Transposta: ')
for i in range (colunas):
    for j in range (linhas):
        print(f'{transposta[i][j]:4}',end=' ')
    print('')