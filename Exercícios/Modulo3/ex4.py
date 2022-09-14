import requests

respose = requests.get('https://swapi.dev/api/people/4/').json()
print(respose['name'])

darthVader = {
    'nome': respose['name'],
    'altura': respose['height'],
    'massa': respose['mass'],
    'nascimento': respose['birth_year'],
    'genero': respose['gender']
}

print(darthVader)