pergunta1 = input('Mora perto da vítima? sim/não ')
pergunta2 = input('já trabalho com a vítima? sim/não ')
pergunta3 = input('telefonou para a vítima? sim/não ')
pergunta4 = input('esteve no local do crime? sim/não ')
pergunta5 = input('deveia para vítima? sim/não ')

perguntas = [pergunta1,pergunta2,pergunta3,pergunta4,pergunta5]
supeitas = 0
for res in perguntas:
    if res.lower() == 'sim':
        supeitas = supeitas + 1

if supeitas == 5:
    print('É o assasino!')
elif supeitas == 4 or supeitas == 3:
    print('É cumplice!')
elif supeitas == 2:
    print('É suspeito!')
else:
    print('Liberar!')



