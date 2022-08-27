#Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima sua classificação: vogal, consoante, número e caractere especial.

entrada = input('Digite um caractere: ')
caractere = entrada.lower()
if caractere >= 'a' and caractere <= 'z':
    if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
        print('Vogal.')
    else:
        print('Consoante.')
else:
    if caractere >= '0' and caractere <= '9':
        print('Número.')
    else:
        print('Caractere especial.')