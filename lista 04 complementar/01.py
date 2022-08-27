'''
Escreva um programa que leia um vetor contendo N elementos inteiros (N será lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.
'''

import random
tamanho = int(input('Tamanho do vetor: '))
vetorA = [None] * tamanho

for i in range (tamanho):
    vetorA[i] = random.randint(1, 20)
print(f'Vetor A: {vetorA}')

contadorpares = 0
contadorimpares = 0
somador = 0
media = 0

for i in range (tamanho):
    if vetorA[i] % 2 == 0:
        contadorpares += 1
    else:
        contadorimpares += 1
    somador += vetorA[i]
media = somador / tamanho

print(f'Quantidade de elementos pares no vetor: {contadorpares}')
print(f'Quantidade de elementos impares no vetor: {contadorimpares}')
print(f'A soma de todos os elementos é: {somador}')
print(f'A média dos elementos do vetor é: {media}')