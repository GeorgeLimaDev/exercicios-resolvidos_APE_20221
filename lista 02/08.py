#Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir "Operador desconhecido".
print('Operações disponíveis: \n Soma = +, \n Subtração = -, \n Multiplicação = *, \n Divisão = /.')
operacao = input('Digite a operação desejada: ')
if operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/':
    print('Operador desconhecido.')
resultado = 0
if operacao == '+':
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))
    resultado = num1 + num2
    print('Resultado: ', resultado)
elif operacao == '-':
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))
    resultado = num1 - num2
    print('Resultado: ', resultado)
elif operacao == '*':
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))
    resultado = num1 * num2
    print('Resultado: ', resultado)
elif operacao == '/':
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))
    resultado = num1 / num2
    print('Resultado: ', resultado)