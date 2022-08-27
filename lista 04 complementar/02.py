#Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a intercalação dos elementos de A e B. Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]

import random
tamanho = int(input('Tamanho do vetor: '))
vetorA = [None] * tamanho
vetorB = [None] * tamanho
vetorC = [None] * (tamanho * 2)

for i in range (tamanho):
    vetorA[i] = random.randint(1, 20)
    vetorB[i] = random.randint(1, 20)

#A multiplicação faz com que o índice acessado siga a ordem normal (0,1,2...n)
for i in range (tamanho):
    vetorC[i*2] = vetorA[i]
    vetorC[i*2+1] = vetorB[i]

print(f'Vetor A: {vetorA}')
print(f'Vetor B: {vetorB}')
print(f'Vetor C: {vetorC}')