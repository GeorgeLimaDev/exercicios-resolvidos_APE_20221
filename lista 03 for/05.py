'''
Faça um programa que, para um grupo de N pessoas (obs: N será lido):
• Leia o sexo (M ou F) de cada pessoa;
• Calcule e escreva o percentual de homens;
• Calcule e escreva o percentual de mulheres.
'''

total = int(input('Total de pessoas: '))
conthomens = 0
contmulheres = 0
for i in range (total):
    sexo = input('Sexo da pessoa (M ou F): ')
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F':
        contmulheres += 1

perchomens = (conthomens / total) * 100
percmulheres = (contmulheres / total) * 100

print(f'Percentual de homens: {perchomens}%.')
print(f'Percentual de mulheres: {percmulheres}%.')