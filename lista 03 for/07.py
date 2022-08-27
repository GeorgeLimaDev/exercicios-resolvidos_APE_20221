#Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Faça um programa que leia um número e determine se ele é ou não primo.

numero = int(input('Número: '))
for i in range (2, numero):
    if numero % i == 0:
        primo = False
    else:
        primo = True
if primo:
    print('O número é primo.')
else:
    print('O número não é primo.')