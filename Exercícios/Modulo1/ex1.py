input = float(input('Forneça um valor: '))

def printvalue(value):
    newValue = value * 0.85
    print(f'O novo valor é {int(newValue)}')

printvalue(input)