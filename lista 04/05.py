#Escreva um programa que receba um vetor V de N números inteiros (N será lido), determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices. Obs: suponha a inexistência de valores repetidos.

tamanho = int(input('Tamanho do vetor: '))
vetorA = [None] * tamanho

for i in range (tamanho):
    vetorA[i] = int(input('Elemento: '))

maior = vetorA[0]
indicemaior = 0
menor = vetorA[0]
indicemenor = 0

for i in range (1, tamanho):
    if vetorA[i] > maior:
        maior = vetorA[i]
        indicemaior = i
    if vetorA[i] < menor:
        menor = vetorA[i]
        indicemenor = i

print(f'Vetor: {vetorA}')
print(f'Maior: {maior}')
print(f'Posição do maior: {indicemaior}')
print(f'Menor: {menor}')
print(f'Posição do menor: {indicemenor}')