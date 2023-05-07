guests = ['amigos', 'familiares', 'inimigos']
not_come = 'inimigos'
guests.append('melhores amigos')
#acrescentando elementos em uma lista

print('Gostaria de convidar para um jantar meus ' + guests[0] + '.')
print('Gostaria de convidar para um jantar meus ' + guests[1] + '.')
print('Meus ' + not_come + ' não vão participar do jantar.')
print('Mas temos novos convidos, meus ' + guests[-1] + '!')

print('-------------------------------------------')
print(f'Olá, meus {guests[0]}! Vocês querem jantar comigo?')
print(f'Olá, meus {guests[1]}! Vocês querem jantar comigo?')
print(f'Olá, meus {guests[-1]}! Vocês querem jantar comigo?')
