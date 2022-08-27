#Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metros e cresce 3 centímetros por ano. Faça um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.

alturachico = 150
alturaze = 110
crescimentochico = 2
crescimentoze = 3
contador = 0
while alturachico > alturaze:
    alturachico += crescimentochico
    alturaze += crescimentoze
    contador += 1
print(f'O tempo necessário para que a altura de Zé seja maior que a de Chico é de {contador} anos.')