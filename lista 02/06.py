#Recomendam-se estudantes para bolsas de estudo em função de seu desempenho. A natureza das recomendações é baseada na seguinte tabela: A = Fortemente recomendado; B ou C = Recomendado; D = Não recomendado.
nome = input('Nome do estudante: ')
conceito = input('Conceito deste estudante: ').upper()
if conceito == 'A':
    print('Fortemente recomendado.')
elif conceito == 'B' or conceito == 'C':
    print('Recomendado.')
else:
    print('Não recomendado.')