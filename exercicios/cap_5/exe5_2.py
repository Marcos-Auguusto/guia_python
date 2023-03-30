cores = input('Qual é a sua cor favorita?')

if cores.lower() == 'verde':
    print('True')
else:
    print('False')
    
age = input('Quantos anos você tem? ')
if age == '':
    ageTwo = input('Por favor, digite sua idade! ') 
    if ageTwo == '':
        exit()

for inputAge in age:
    age = int(age)

    if age >= 18:
        print('Você é maior de idade. Pode beber a vontade!')
    else:
        print('Você não é maior de idade. Crie juizo!')
        exit()

produto = 18.00
myMoney = input('Quanto eu tenho para gastar? ')
floatMyMoney = float(myMoney)


if (floatMyMoney >= produto) or (floatMyMoney >= 18):
    print('Tenho dinheiro para a aquilo!!!')
else:
    print('Não tenho dinheiro para aquilo, sou um coitado!')

produtos = ['cerveja', 'vodka', 'coca-cola']

'cerveja' in produtos
print('True')




