import csv

linhasArquivo = []
with open('Exercícios/Modulo3/alunos.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        linhasArquivo.append(linha)

linhasArquivo[0].append('Média')
for linha in range(len(linhasArquivo)):
    if linha != 0:
        media = (
            float(linhasArquivo[linha][3]) + 
            float(linhasArquivo[linha][4]) + 
            float(linhasArquivo[linha][5]) + 
            float(linhasArquivo[linha][6])
            ) /4
        linhasArquivo[linha].append(media)

with open('Exercícios/Modulo3/alunos_copia.csv', 'w') as arquivo_copia:
    leitor = csv.writer(arquivo_copia)
    leitor.writerows(linhasArquivo)