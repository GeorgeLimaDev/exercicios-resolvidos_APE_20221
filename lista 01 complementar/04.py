'''
Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem, bem como o número de litros de combustível gastos.
Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a capacidade do tanque e mostre:
a) Quilometragem rodada.
b) Quantos quilômetros por litro faz o veículo.
c) Autonomia do veículo.
d) Custo da viagem.
'''
kminicial = float(input('Hodômetro inicial (Kms): '))
kmfinal = float(input('Hodômetro final (Kms): '))
gastos = float(input('Total de combustível gasto (litros): '))
preco = float(input('Preço do litro de combustível (R$): '))
tanque = float(input('Capacidade do tanque (Litros): '))

distancia = kmfinal - kminicial
rendimento = distancia / gastos
autonomia = distancia / (tanque - gastos)
custo = preco * gastos

print('-'*25)
print(f'Quilometragem rodada na viagem: {distancia:.2f} Kms.')
print(f'Rendimento: {rendimento:.2f} Kms/L.')
print(f'Autonomia do veículo: {autonomia:.2f} Kms/L')
print(f'Custo total da viagem: R$ {custo:.2f}.')