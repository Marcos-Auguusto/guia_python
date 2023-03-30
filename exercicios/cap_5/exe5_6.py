ageInput = input('Quantos anos você tem? ')
age = int(ageInput)

if age < 2:
    print('Você é um bebê!')
elif age >= 2 and age < 4:
    print('Você é um(a) criança!')
elif age >= 4 and age < 13:
    print('Você é um(a) garoto(a)!')
elif age >= 13 and age < 20:
    print('Você é um(a) adolescente!')
elif age >= 20 and age < 65:
    print('Você é um(a) adulto!')
elif age > 65:
    print('Você é um(a) idoso')
else:
    retInputAge = input('Tente novamente: ')