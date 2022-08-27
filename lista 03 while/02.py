#Faça um programa que leia vários números, calcule e exiba a média desses números. Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser computado na média)

flag = 999
total = 0
contador = 0
while True:
    numero = int(input('Número (999 para encerrar): '))
    if numero < 999:
        total += numero
        contador += 1
    if numero == flag:
        break
media = total / contador
print(f'A média dos números digitados é: {media}')