#Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.

import random

tamanho = int(input('Tamanho do vetor: '))
vetorA = [None] * tamanho
numero = int(input('Número a localizar no vetor: '))
contador = 0

for i in range (tamanho):
    vetorA[i] = random.randint(1, 10)

for i in range (tamanho):
    if vetorA[i] == numero:
        contador += 1

print('-'*50)
print(vetorA)
print(f'O número de ocorrência de {numero} no vetor é: {contador}.')