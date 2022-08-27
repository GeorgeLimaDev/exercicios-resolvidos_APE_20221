#Faça um programa que, leia a temperatura dos 30 dias do mês de abril diga qual o dia mais quente e o dia mais frio do mês (obs: suponha que não haja empates).

contador = 0
maior = 0
menor = 999
while contador <= 5:
    temperatura = int(input('Temperatura: '))
    if temperatura > maior:
        maior = temperatura
        contador += 1
        diaquente = contador
    elif temperatura < menor:
        menor = temperatura
        contador += 1
        diafio = contador
    else:
        contador += 1

print(f'O dia mais quente do ano foi {diaquente} com uma temperatura de {maior}')
print(f'O dia mais frio do ano foi {diafio} com uma temperatura de {menor}')