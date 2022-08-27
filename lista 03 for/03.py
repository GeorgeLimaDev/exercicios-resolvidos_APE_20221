#Faça um programa que calcule e mostre o fatorial de um número N, fornecido pelo usuário. A definição de fatorial é a multiplicação de todos os termos até o termo lido.

numero = int(input('Número: '))
fatorial = 1
for i in range (2, numero+1):
    fatorial = fatorial * i
    
print(f'{numero}!: {fatorial}')