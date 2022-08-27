#O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Faça um programa que leia o peso do prato montado pelo cliente (em quilos) e exiba o valor a pagar. Assuma que a balança já desconte o peso do prato.
quilo = 25
peso = float(input('Digite o peso do prato (Kgs): '))
resultado = peso * quilo
print(f'O preço deste prato é: R$ {resultado}.')