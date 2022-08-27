#Faça um programa que acompanhe um set de uma partida de vôlei. O programa deve ler o código da equipe (A ou B) que ganhou o ponto e responder quem ganha a partida. O set chega ao final se uma das equipes chega a 25 pontos e a diferença de pontos entre elas é maior ou igual a dois. A equipe que conseguir isso é a vencedora do set.

totalA = 0
totalB = 0
diferenca = 0
flag = 5
while True:
    equipe = input('Quem pontuou? (A/B): ').upper()
    if equipe == 'A':
        totalA += 1
    if equipe == 'B':
        totalB += 1
    print(f'Placar parcial: {totalA} x {totalB}')
    if totalA > totalB:
        diferenca = totalA - totalB
    if totalB > totalA:
        diferenca = totalB - totalA
    if (totalA > flag or totalB >= flag) and (diferenca >= 2):
        break
print(f'Placar final: {totalA} x {totalB}')
if totalA > totalB:
    print('A equipe A venceu!')
else:
    print('A equipe B venceu!')