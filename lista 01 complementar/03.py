#Escreva um programa que leia duas variáveis inteiras e troque o conteúdo entre elas, mostrando o resultado.
entrada1 = int(input('Digite o primeiro número: '))
entrada2 = int(input('Digite o segundo número: '))
intermedio = entrada1
entrada1 = entrada2
entrada2 = intermedio
print(f'Conteúdo final em entrada1: {entrada1}')
print(f'Conteúdo final em entrada2: {entrada2}')