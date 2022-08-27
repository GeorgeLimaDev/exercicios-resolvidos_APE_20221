#Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-se que nota1 possui peso 6 e nota2 possui peso 4.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
resultado = ((nota1 * 6) + (nota2 * 4) / 2) / 10
print(f'A média ponderada é: {resultado:.2f}.')