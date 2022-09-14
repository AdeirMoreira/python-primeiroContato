valueStrings = input('Digite alguns números separados por virgula: ')
valuesList = valueStrings.split(',')
for i in range(len(valuesList)):
    valuesList[i] = int(valuesList[i])

pairscont = 0
pairslist = []
for i in valuesList:
    if i % 2 == 0:
        pairscont = pairscont + 1
        pairslist.append(i)

print(f'Você digitou {pairscont} numeros pares, são eles {pairslist}')