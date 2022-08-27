'''
Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.
'''

import random
vetorA = [None] * 10
for i in range (len(vetorA)):
    vetorA[i] = random.randint(1,10)
print(f'Vetor completo: {vetorA}')
print('Números nos índices pares:')
for i in range (0,len(vetorA),2):
        print(vetorA[i],end=' ')
print('\nNúmeros nos índices impares:')
for i in range (1,len(vetorA),2):
    print(vetorA[i],end=' ')