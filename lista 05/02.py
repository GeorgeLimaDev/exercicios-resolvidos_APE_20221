'''
Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
'''

import random
tamanho = int(input('Tamanho da matriz quadrada: '))
matrizA = [[None] * tamanho for i in range (tamanho)]

for i in range (tamanho):
    for j in range (tamanho):
        matrizA[i][j] = random.randint(1, 20)

print('Matriz A: ')
for i in range (tamanho):
    for j in range (tamanho):
        print(f'{matrizA[i][j]:4}',end=' ')
    print('')

principal = [None] * tamanho
for i in range (tamanho):
    for j in range (tamanho):
        if matrizA[i] == matrizA[j]:
            principal[i] = matrizA[i][j]
print(f'Diagonal principal da matriz: {principal}')