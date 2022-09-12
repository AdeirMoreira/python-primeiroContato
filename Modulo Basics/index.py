print("hellow World!")

x = 5 
print(x)
print(type(x))
preco = 19.99
print(preco, type(preco))
cidade = 'são paulo'
print(cidade,type(cidade))
boleano = True
print(type(boleano))

x = 50
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x ** y)
print(x // y)
print(x % y)

e_segunda = True
e_domingo = False
print(not e_segunda, e_segunda)
print(e_segunda and e_domingo)
print(e_segunda or e_domingo)

dolar = 5
real = 1
print(dolar >= real)
print(dolar <= real)
print(dolar == real)
print(dolar != real)
idade = int(input('qual a sua idade? '))
print(idade, type(idade))
print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(-5))

salario = float(input('Qual seu salario? '))
gasto = float(input('Qual seu gasto? '))
print('Ao final do ano você tera', (salario * 12 ) - (gasto * 12))

passagem = 6.75
corrida = float(input("Qual o valor da corrida? "))
if corrida <= passagem * 5:
    print('Pegue a corrida!')
elif corrida <= passagem * 6:
    print('Aguarde!')
else:
    print('Pegue o onibus!')

contador = 0
while contador < 10:
    contador = contador + 1
    if(contador == 1):
        print(contador, 'item limpo!')
    else: 
        print(contador,'itens limpos!')
print('você terminou!')

while True:
    if contador < 10:
        contador = contador + 1
        if(contador == 1):
            print(contador, 'item limpo!')
        else: 
            print(contador,'itens limpos!')
    else:
        break
print('você terminou!')

senha = input('Digite seua senha: ')

while senha != 'letscode':
    print('senha incorreta, tente novamente!')
    senha = input('Digite seua senha: ')
print('acesso permitido!')

while contador < 10:
    contador = contador + 1
    if(contador % 2 == 1):
        continue
    else: 
        print(contador,'itens limpos!')
print('você terminou!')