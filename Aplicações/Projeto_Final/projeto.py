import csv
import requests as r
import datetime as dt
from PIL import Image

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
DATE = 4

for i in range(1, len(dadosUteis)):
    dadosUteis[i][DATE] = dadosUteis[i][DATE][:10]

with open('Aplicações/Projeto_Final/brasil_covid.csv', 'w') as arquivo: 
    escrever = csv.writer(arquivo)
    escrever.writerows(dadosUteis)

for i in range(1, len(dadosUteis)):
    dadosUteis[i][DATE] = dt.datetime.strptime(dadosUteis[i][DATE], '%Y-%m-%d')
# print(dadosUteis)

def get_dataSets(y,labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label' : labels[i],
                'data' : y[i]
            })
        return datasets
    else:
        return [
            {
                'label' : labels[0],
                'data' : y
            }
        ]

def setTitle (title = ''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title' : title,
        'display' : display
    }

def create_chart(x,y,labels, type='bar',title=''):
    datasets = get_dataSets(y,labels)
    options = setTitle(title)
    chart = {
        'type': type,
        'data': {
            'labels' : x,
            'datasets' : datasets
        },
        'options' : options
    }
    return chart

def get_API_Chart(chart):
    baseURL = 'https://quickchart.io/chart'
    response = r.get(f'{baseURL}?c={str(chart)}')
    return response.content

def save_image(path, content):
    with open(path , 'wb') as image:
        image.write(content)

y_data1 = []
for data in dadosUteis[1::30]:
    y_data1.append(data[CONFIRMADOS])

y_data2 = []
for data in dadosUteis[1::30]:
    y_data2.append(data[OBITOS])

labels = ['Confirmados', 'Óbitos']

x = []
for data in dadosUteis[1::30]:
    x.append(data[DATE].strftime('%d/%m/%Y'))

chart = create_chart(x,[y_data1,y_data2],labels,title='Gráfico Confirmados X Óbitos')
chart_content = get_API_Chart(chart)
save_image('Aplicações/Projeto_Final/graficoImg.png', chart_content)

