#Faça um programa que leia os seguintes dados de um conjunto de alunos: matrícula, nome e as duas notas que ele obteve em suas avaliações. A condição de parada será a digitação de uma matrícula igual 0 (zero). O programa deverá mostrar, para cada aluno, as seguintes informações: matrícula, nome, média e situação (aprovado, se a média for igual ou superior a 7 e, reprovado, se a média for inferior a 7).

flag = 0
matricula = int(input('Matrícula: '))
while matricula != flag:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    if media >= 7:
        conceito = 'Aprovado'
    else:
        conceito = 'Reprovado'
    print(nome, matricula, media, conceito)
    matricula = int(input('Matrícula: '))
print('Fim do programa.')