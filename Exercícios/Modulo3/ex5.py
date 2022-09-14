import requests

respose = requests.get('https://api.covid19api.com/country/brazil').json()

for day in respose:
    if day['Confirmed'] == 1:
        day = day['Date'][:10]
        day = day.split('-')
        day.reverse()
        dayreverted = '/'.join(day)
        print(f'O primeiro caso de covid resgistrado no brasil ocorreu dia {dayreverted}')
        break