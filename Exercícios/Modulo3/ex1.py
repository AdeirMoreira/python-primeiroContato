import csv

with open('Exercícios/Modulo3/alunos.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)