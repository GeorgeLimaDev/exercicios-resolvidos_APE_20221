'''
A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$ 1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do valor da venda.
Escreva um programa que leia o nome, o número de carros vendidos e o valor total das vendas de um vendedor, e calcule e exiba o seu salário.
'''
salario = 1000
nome = input('Digite seu nome: ')
vendas = int(input('Quantos carros foram vendidos por você? '))
total = float(input('Digite o valor total das vendas: '))
comissao = vendas * 200
adicional = total / 20
resultado = salario + comissao + adicional
print(f'O vendedor {nome} totalizou um salário de R$ {resultado}.')