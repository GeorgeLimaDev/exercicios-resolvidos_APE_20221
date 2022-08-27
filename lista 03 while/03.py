#Faça um programa que leia vários números, determine e mostre o maior e o menor deles. Obs: a leitura do número 0 (zero) encerra o programa.

numero = int(input('Número (0 para parar): '))
flag = 0
maior = numero
menor = numero
while numero != flag:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    numero = int(input('Número (0 para parar): '))
    
print('O maior número é: ', maior)
print('O menor número é: ', menor)
