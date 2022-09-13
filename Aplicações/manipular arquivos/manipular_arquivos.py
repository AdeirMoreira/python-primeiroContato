arquivo = open('Aplicações/ponto_de_exclamacao.txt', 'r')
texto = arquivo.read()
print(texto)
arquivo.close()

linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

for linha in arquivo:
    print(linha, end='')
arquivo.close()

with open('Aplicações/ponto_de_exclamacao.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto)

with open('Aplicações/cante_por_nos.txt', 'w') as arquivo1:
    arquivo1.write('Sexta feira é dia de molhar os pés\n')
    arquivo1.write('Deitar na rede, o cobertor no corpo sem stress\n')
    arquivo1.write('E deixa o vento refrescar\n')

with open('Aplicações/cante_por_nos.txt', 'a') as arquivo2:
    arquivo2.write('Eu toco violão pra gente descansar\n')
    arquivo2.write('Enquanto bate palma, sempre na calma, amor\n')
    arquivo2.write('Vamo lavar a alma\n')
    arquivo2.write('Hoje eu não vou ter insônia\n')
    arquivo2.write('Teu sorriso me livra da Babilônia\n')