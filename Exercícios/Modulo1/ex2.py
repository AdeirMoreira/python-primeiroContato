idade = int(input('Qual sua idade? '))
while idade < 0 or idade > 50:
    print('Sua idade deve ser entre 0 e 50')
    idade = int(input('Qual sua idade? '))
    
salario = int(input('Qual seu salário? '))
while salario < 0:
    print('Seu salario deve ser maior que 0')
    salario = int(input('Qual seu salário? '))


sexo = input('Qual seu sexo? ')
while sexo.upper() != 'M' and sexo.upper() != 'F' and sexo.lower() != 'outro':
    print(sexo)
    print('O sexo deve ser "M" ou "F" ou "Outro"')
    sexo = input('Qual seu sexo? ')