import csv
import requests as r
import datetime as dt

url = 'http://api.covid19api.com/dayone/country/brazil'
response = r.get(url).json()

dadosUteis = []
dadosUteis.insert(0,['Confirmados', 'Obitos', 'Recuperados', 'Ativos', 'Data'])
for data in response:
    dadosUteis.append([
        data['Confirmed'],
        data['Deaths'],
        data['Recovered'],
        data['Active'],
        data['Date']
        ])
# print(dadosUteis)

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(dadosUteis)):
    dadosUteis[i][DATA] = dadosUteis[i][DATA][:10]

with open('Aplicações/Projeto_Final/brasil_covid.csv', 'w') as arquivo: 
    escrever = csv.writer(arquivo)
    escrever.writerows(dadosUteis)

for i in range(1, len(dadosUteis)):
    dadosUteis[i][DATA] = dt.datetime.strptime(dadosUteis[i][DATA], '%Y-%m-%d')
print(dadosUteis)

