import requests

nomedopokemom = input('Quem pokemom você quer ver? ')

url = f'https://pokeapi.co/api/v2/pokemon/{nomedopokemom}'
req = requests.get(url).json()
pokeom = {
    'id': req['id'],
    'nome': req['name'],
    'altura': req['height'],
    'peso': req['weight'],
    'tipo': req['types'][0]['type']['name']
}
print(pokeom)