#Faça um programa que leia um número N, calcule e mostre os N primeiros termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). O valor lido para N sempre será maior ou igual a 2.


print('Exibir sequência de Fibonacci. \nDigite o número de elementos a exibir.')
numero = int(input('Número: '))
a = 0
b = 1
print('Sequência de Fibonacci: ',a, b, end=' ')

for i in range (3, numero+1):
    c = a + b
    print(c, end=' ')
    a = b
    b = c