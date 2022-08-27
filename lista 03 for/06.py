#Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os números múltiplos de N entre X e Y.

numero1 = int(input('Número a ser calculado: '))
numero2 = int(input('Início do intervalo: '))
numero3 = int(input('Fim do intervalo: '))
for i in range (numero2, numero3+1):
    if i % numero1 == 0:
        print(i, end=' ')