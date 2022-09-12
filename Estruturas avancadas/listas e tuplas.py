times = ['Atlético', 'Cruzeiro', 'América', 'Flamengo', 'São Paulo', 'Corinthians']
print(times)
print('tamanho da lista:', len(times))
print('meu time ', times[0])
print('america, ', times[2])
times[1] = 'Palmeiras'
print(times)
print(times[2:5])
print(times[1:-1])
print(times[:-1])
print(times[::2])
print(times[::-1])
print('Atlético' in times)
print('Cruzeiro' not in times)

paises = []
print(paises)
paises.append('Brasil')
print(paises)
paises.append('China')
print(paises)
paises.insert(1 ,'Russia')
print(paises)
paises.remove('Russia')
print(paises)
removido = paises.pop(0)
print(paises)
print(removido)

times_com_tupla = 'Atlético', 'Cruzeiro', 'América', 'Flamengo', 'São Paulo', 'Corinthians'
print(times_com_tupla, type(times_com_tupla), len(times_com_tupla))
print(times_com_tupla[2])
a, cr, am, f, s, co  = times_com_tupla
print(cr,f)
print(*times_com_tupla)