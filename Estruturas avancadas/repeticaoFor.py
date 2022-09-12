Linguagens = ['Javascript', 'Python', 'Java', 'SQL', 'Goolang', 'Ruby']
for lan in Linguagens:
    print(lan)

pessoa = {
    'nome' : 'adeir',
    'idade': 27,
    'liguagens': ['JavaScript', 'Python', 'SQL']
}

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')

for posicao in range(len(Linguagens)):
    Linguagens[posicao] = None
print(Linguagens)
print(list(range(10)))
print(list(range(3,10)))
print(list(range(0,10,2)))