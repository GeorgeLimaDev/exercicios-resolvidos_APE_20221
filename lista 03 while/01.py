#Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles Obs: não use o comando for, use while.

contador = 0
total = 0
while True:
    numero = int(input('Número: '))
    total += numero
    contador += 1
    if contador == 30:
        break
print('A soma dos números digitados é: ', total)