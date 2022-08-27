#Escreva um programa para ler 6 números. Após a leitura dos números, verifique, para cada um deles, se é distinto, ou seja, não possui repetição.

import random
tamanho = 6
vetorA = [None] * tamanho

for i in range (tamanho):
    vetorA[i] = random.randint(1,10)

comparador = vetorA[0]
contador = 0
for i in range (1, tamanho):
    if comparador == i:
        print('O número se repete.')
    else:
        print('O número não se repete.')
    contador += 1
    if contador == 5 or contador == 10 or contador  == 15 or contador == 20 or contador == 25:
        comparador = vetorA[comparador+1]

#Tem um erro na hora de atribuir o índice seguinte ao comparador.