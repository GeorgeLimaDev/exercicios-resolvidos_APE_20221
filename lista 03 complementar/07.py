'''
Uma certa empresa pretende verificar se os seus empregados estarão qualificados ou não para aposentadoria em 2022.
Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
• Ter no mínimo 65 anos de idade; ou
• Ter trabalhado no mínimo 30 anos; ou
• Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
Com base nas informações acima, faça um programa para:
• Ler o nome do empregado, o ano de nascimento e o ano de seu ingresso na empresa.
• Calcular e exibir a idade e o tempo de trabalho do empregado (estimado ao final de 2021)
• Exibir a mensagem “Pode Requerer Aposentadoria” se atender aos requisitos ou “Não Pode Requerer Aposentadoria” caso contrário.
Ao final de cada execução, o programa deverá perguntar se o usuário deseja fazer nova verificação. Se sim, o programa deverá repetir tudo novamente, caso contrário deverá encerrar.
'''

flag = 'N'
continuar = 'S'
while continuar != flag:
    nome = input('Nome: ')
    ano = int(input('Ano de nascimento: '))
    anoingresso = int(input('Ano de ingresso: '))
    if (2021 - ano) >= 65 or (2021 - anoingresso) >= 30:
        print('Pode se aposentar.')
    elif (2021 - ano) >= 60:
        if (2021 - anoingresso) >= 25:
            print('Pode se aposentar.')
    else:
        print('Ainda não pode se aposentar.')
    continuar = input('Continuar? (S/N): ')