'''
Escreva um programa que:
• Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma turma e a média de cada um deles.
o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
o As médias serão calculadas e armazenadas na 4ª coluna da matriz.
• Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
• Calcule e imprima a média geral da turma.
• Calcule e imprima o número de alunos com média superior à média geral da turma.
'''

linhas = 3
colunas = 4
matriz = [[None] * colunas for i in range (linhas)]

for i in range (linhas):
    for j in range (colunas-1):
        matriz[i][j] = int(input('Nota: '))

for i in range (linhas):
    media = 0
    for j in range (colunas):
        media = (matriz[i][0] + matriz[i][1] + matriz[i][2]) / 3
        matriz[i][3] = media

print('Matriz: ')
for i in range (linhas):
    for j in range (colunas):
        print(f'{matriz[i][j]:4}',end=' ')
    print('')

mediageral = 0
for i in range (linhas):
    for j in range (colunas):
        mediageral += matriz[i][3] / linhas
print(f'Media geral da turma: {mediageral}')

#Falta arrumar a média geral e terminar a questão.