#Faça um programa que leia um número N, inteiro, e some todos os números de 1 até N, mostrando o resultado.

from re import I


numero = int(input('Número: '))
somador = 0
for i in range (numero+1):
    somador += i
print(f'A soma de todos os termos até {numero} é: {somador}')