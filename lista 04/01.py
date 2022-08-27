#Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K. Ex: A = [1,2,3], K = 5, B = [5,10,15].

tamanho = int(input('Tamanho dos vetores: '))
multiplicador = int(input('Multiplicador: '))
vetorA = [None] * tamanho
vetorB = [None] * tamanho

for i in range (tamanho):
    vetorA[i] = int(input('Elemento: '))
for i in range (tamanho):
    vetorB[i] = vetorA[i] * multiplicador

print(f'Vetor A: {vetorA}')
print(f'Vetor B: {vetorB}')