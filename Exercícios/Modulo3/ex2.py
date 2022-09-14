import csv

linhasArquivo = []
with open('Exercícios/Modulo3/alunos.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        linhasArquivo.append(linha)

with open('Exercícios/Modulo3/alunos_copia.csv', 'w') as arquivo_copia:
    leitor = csv.writer(arquivo_copia)
    leitor.writerows(linhasArquivo)



