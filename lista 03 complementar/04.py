#Um dado material radioativo perde metade de sua massa a cada 50 segundos. Faça um programa que leia uma certa quantidade de massa, em gramas, deste material e imprima o tempo necessário para que sua massa se torne menor que 0.5g.

quantidademassa = int(input('Quantidade de massa: '))
contador = 0
while quantidademassa >= 0.5:
    contador += 50
    quantidademassa /= 2
print(f'O tempo necessário para a massa do elemento ser menor que 0.5g é: {contador}s.')