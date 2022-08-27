'''
Faça um programa que leia a idade de várias pessoas visitantes de um show (a leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
• A média de idade do público;
• A porcentagem de pessoas com idade entre 18 e 21 anos;
• Idade do visitante mais jovem.
'''

media = 0
porcentagem = 0
menor = 999
contador = 0
jovens = 0
somador = 0

while True:
    idade = int(input('Idade do(a) visitante: '))
    if idade == 0:
        break
    contador += 1
    somador += idade
    if idade >= 18 and idade <= 21:
        jovens += 1
        porcentagem = (jovens * 100) / contador
    if idade < menor:
        menor = idade
    media = somador / contador

print(f'Média de idade do público: {media}')
print(f'Porcentagem de jovens: {porcentagem}')
print(f'Idade do visitante mais jovem: {menor}')