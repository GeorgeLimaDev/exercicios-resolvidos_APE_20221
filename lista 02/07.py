#Escreva um programa que leia o peso (kg) e a altura (m) de uma pessoa, determine e mostre o seu grau de obesidade, de acordo com a tabela seguinte. O grau de obesidade é determinado pelo índice de massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa pelo quadrado da sua altura.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(altura)
print(f'Seu IMC é: {imc}')
if imc >= 30:
    print('Obeso mórbido.')
elif imc >= 26 and imc < 30:
    print('Obeso')
elif imc < 26:
    print('Normal.')