#Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma nota maior ou igual a 8.0 para ser aprovado no concurso. Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele foi aprovado ou não no concurso.

nota1 = float(input('Nota 1 da 1. etapa: '))
nota2 = float(input('Nota 2 da 2. etapa: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Apto para segunda etapa.')
    nota3 = float(input('Nota da segunda etapa: '))
    if nota3 >= 8.0:
        print('Aprovado no concurso!')
    if nota3 < 8.0:
        print('Reprovado no concurso.')
else:
    print('Inapto para segunda etapa.')
