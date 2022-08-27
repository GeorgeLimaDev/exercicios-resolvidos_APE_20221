'''
O cardápio de uma casa de lanches, especializada em sanduíches, é dado a seguir.
CÓDIGO
NOME
PREÇO
H
Hamburger
R$ 5,00
C
Cheese Burger
R$ 6,00
B
Cheese Bacon
R$ 7,00
F
Cheese Frango
R$ 4,00
Faça um programa que leia o código e a quantidade de cada item comprado por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao final, calcule e exiba o total a pagar.
Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2 Cheese Bacon:
Entrada:
Código: H
Quantidade: 3
Código: B
Quantidade: 2
Código: X
Saída:
Total a pagar: R$ 29.00
'''

#Cardápio:
hamburger = 'H'
cheeseburger = 'C'
cheesebacon = 'B'
cheesefrango = 'F'

precoH = 5
precoC = 6
precoB = 7
precoF = 4

totalH = 0
totalC = 0
totalB = 0
totalF = 0
total = 0

while True:
    pedido = input('Código: ').upper()
    if pedido == 'X':
        break
    quantidade = int(input('Quantidade: '))
    if pedido == 'H':
        totalH = precoH * quantidade
    if pedido == 'C':
        totalC = precoC * quantidade
    if pedido == 'B':
        totalB = precoB * quantidade
    if pedido == 'F':
        totalF = precoF * quantidade
    total = totalH + totalC + totalB + totalF

print(f'Valor total do pedido: R$ {total}.')