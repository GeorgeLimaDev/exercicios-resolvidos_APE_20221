#Escreva um programa que leia dois números e exiba-os em ordem crescente.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 < numero2:
    print(numero1, numero2)
else:
    print(numero2, numero1)
