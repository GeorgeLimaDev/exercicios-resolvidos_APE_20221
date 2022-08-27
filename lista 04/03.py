#Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver, informe em que posição (índice). Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.

tamanho = int(input('Tamanho do vetor: '))
numero = int(input('Número a localizar no vetor: '))
localizador = False
vetorA = [None] * tamanho

for i in range (tamanho):
    vetorA[i] = int(input('Elemento: '))
for i in range (tamanho):
    if vetorA[i] == numero:
        localizador = True
        if localizador:
            print(f'{numero} aparece em: ',i)