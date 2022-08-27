#Faça um programa que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.
dolares = float(input('Quantos dólares você possui? '))
cotacao = float(input('Digite a cotação atual do dólar: '))
resultado = dolares / cotacao
print(f'O valor em reais é de R$ {resultado:.2f}.')