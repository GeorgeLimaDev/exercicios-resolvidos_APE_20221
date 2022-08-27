'''
Escreva um programa que leia um vetor de N números inteiros (N será lido), inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!
'''

import random
tamanho = int(input('Tamanho do vetor: '))
vetorA = [None] * tamanho

for i in range (tamanho):
    vetorA[i] = random.randint(1,20)
print(vetorA)

secundario = tamanho - 1
for i in range (tamanho // 2):
    auxiliar = vetorA[i]
    vetorA[i] = vetorA[secundario]
    vetorA[secundario] = auxiliar
    secundario = secundario - 1
print(vetorA)