#Faça um programa que leia um número inteiro e determine se ele é par ou ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar (digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve repetir tudo de novo, caso contrário o programa deve ser encerrado.

print('Checador de número par ou impar.')
print('Digite 0 para encerrar o programa')
numero = 1
while True:
    numero = int(input('Número para checar: '))
    if numero == 0:
        break
    if numero % 2 == 0:
        print('O número é par.')
    else:
        print('O número é impar.')
print('Fim do programa.')