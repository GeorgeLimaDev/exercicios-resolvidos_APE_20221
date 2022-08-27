#Faça um programa que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).
nome = input('Nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
resultado = (nota1 + nota2 + nota3) / 3
print(f'O aluno {nome} obteve a média {resultado:.2f}')