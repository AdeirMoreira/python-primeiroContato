import csv

with open ('Aplicações/arquivos_csv/covid.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)
    for linha in leitor:
        if float(linha[2]) > 10000:
            print(linha)

with open('Aplicações/arquivos_csv/users.csv', 'w') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome','sobrenome','email','idade'])
    escritor.writerow(['adeir','moreira','adeir@dev.com',27])

header = ['nome','sobrenome']
dados = []
opt = input('O que deseja fazer? \n1 - Cadastrar\n0 - Sair\n')
while opt != '0':
    nome = input('Qual seu nome? ')
    sobrenome = input('Qual seu sobrenome? ')
    dados.append([nome, sobrenome])
    opt = input('O que deseja fazer? \n1 - Cadastrar\n0 - Sair\n')

print(dados)

with open('Aplicações/arquivos_csv/users.csv', 'w') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(header)
    escritor.writerows(dados)

with open('Aplicações/arquivos_csv/users.csv', 'r') as arquivo_users:
    csv_reader = csv.reader(arquivo_users, delimiter=',')
    for linha in csv_reader:
        print(linha)