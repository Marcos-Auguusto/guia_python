alienColor = ['green', 'yellow', 'red']
score = input('Digite a cor do alien que você acertou: ')

if score.lower() == 'green':
    print('Você acaba de ganhar 5 pontos!')
elif score.lower() == 'yellow':
    print('Você acaba de ganhar 10 pontos!')
elif score.lower() == 'red':
    print('Você acaba de ganhar 15 pontos!')
else:
    print('Não existe um alien com essa cor. Tente novamente.')
    score = input('Digite novamente a cor do alien que você acertou: ')

    