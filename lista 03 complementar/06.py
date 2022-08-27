#Faça um programa que solicite ao usuário uma senha. Caso a senha digitada esteja correta, o programa deverá mostrar senha correta. Caso contrário, o programa deverá mostrar senha incorreta e pedir para o usuário tentar novamente digitar a senha correta. Mas, se o usuário fornecer três senhas incorretas, o programa deverá encerrar a sua execução. (Obs: a senha correta é “abcd”).

senhacorreta = 'abcd'
senha = input('Senha: ')
contador = 0
while senha != senhacorreta:
    contador += 1
    if contador == 3:
        print('Senha bloqueada. Fim do programa.')
        break
    senha = input('Senha: ')
    if senha == senhacorreta:
        print('Senha correta.')
        break