#Faça um programa que calcule e mostre os números múltiplos de 5 do intervalo 50 a 300, juntamente com suas raízes e seus cubos.

import math

numero = 5
coluna1 = 5
coluna2 = 10
coluna3 = 10
print(f'{"X":>{coluna1}} {"Raiz(X)":>{coluna2}} {"Cubo(X)":>{coluna3}}')
for i in range (50, 300+1):
    if i % numero == 0:
        raiz = math.sqrt(i)
        cubo = i ** 3
        print(f'{i: {coluna1}} {raiz: {coluna2}.4f} {cubo: {coluna3}}')