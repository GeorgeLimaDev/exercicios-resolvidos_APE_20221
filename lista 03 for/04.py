#Faça um programa que leia 20 números inteiros, determine e mostre o maior deles.

maior = 0
for i in range (20):
    numero = int(input('DIgite o número: '))
    if numero > maior:
        maior = numero

print(f'O maior número digitado é: {maior}')