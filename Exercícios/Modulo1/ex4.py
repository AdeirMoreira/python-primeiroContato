valor = int(input('Qual valor da tabuada vocer quer ver? '))

contador = 0
while contador <= 10:
    print(f'{valor} x {contador} = {valor * contador}')
    contador = contador + 1