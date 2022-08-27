'''
Escreva um programa que, dado um número inteiro representando uma quantidade de segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade.
Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.
'''
total = int(input('Quantidade de segundos: '))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f'Resultado: {horas} horas, {minutos} minutos e {segundos} segundos.')