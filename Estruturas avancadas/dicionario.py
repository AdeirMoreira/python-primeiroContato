pessoa = {
    'nome' : 'adeir',
    'idade': 27,
    'liguagens': ['JavaScript', 'Python', 'SQL']
}
print(pessoa, type(pessoa))
pessoa['área'] = 'Front end'
pessoa['área'] = 'Back end'
print(pessoa)

outrapessoa = pessoa.copy()
outrapessoa['nome'] = 'lilian'
outrapessoa['idade'] = 20
outrapessoa['liguagens'] = ['React', 'flutter', 'nextjs']
outrapessoa['área'] = 'front - end'
print(pessoa,outrapessoa)

informaçoespessoais = {
    'nascimento' : '12/12/1994',
    'nacionalodade' : 'brasileiro'
}

pessoa.update(informaçoespessoais)
print(pessoa)
print(pessoa.get('signo'))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
