#Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de semana (sábado e domingo). Considere que o dia 1 é o domingo.

numero = int(input('Digite o número equivalente ao dia: '))
if numero == 2 or numero == 3 or numero == 4 or numero == 5 or numero ==6:
    print('É dia útil.')
else:
    print('Não é dia útil')
if numero == 1:
    print('Domingo.')
elif numero == 2:
    print('Segunda-feira.')
elif numero == 3:
    print('Terça-feira.')
elif numero == 4:
    print('Quarta-feira.')
elif numero == 5:
    print('Quinta-feira.')
elif numero == 6:
    print('Sexta-feira.')
elif numero == 7:
    print('Sábado.')
else:
    print('Domingo.')