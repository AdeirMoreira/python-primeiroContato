empresa  = 'Google'
print(empresa)

empresa = "Let'sCode"
print(empresa)

frase = "O professor disse: \"Hoje é sexta feira\""
print(frase)

empresa = 'Google'
print(empresa[0])
print(empresa[:3])

cidades = 'Brasília, Belo Horiznonte, São paulo, Rio de Janeiro'
print(cidades)
cidades = cidades.split(', ')
print(cidades)

cabecalho = '                      Menu                           '
print(cabecalho)
cabecalho = cabecalho.strip()
print(cabecalho)

texto = 'BeLo HoRiZoNtE'
print(texto.title())
print(texto.capitalize())
print(texto.upper())
print(texto.lower())

bh = input('Qual a capital da Replública do Pão de Queijo? ')
while bh.lower() != 'belo horizonte':
    print('Errado, tente denovo')
    bh = input('Qual a capital da Replública do Pão de Queijo?')
print('Uai, ta certo!')
print('Belo' in bh)