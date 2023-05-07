guests = ['amigos', 'familiares', 'inimigos']
guests.insert(3,'melhores amigos')
guests.insert(1,'conhecidos')
guests.insert(2,'irmãos da igreja')
guests.append('amigos da faculdade')
#inserindo elementos em uma lista

print(f'Então meus {guests[0]}, encontrei uma mesa com mais espaço.')
print(f'Então meus {guests[1]}, encontrei uma mesa com mais espaço.')
print('--------------------------------------------')

print('Gostaria de convidar para um jantar meus ' + guests[-1] + '.')
print('Gostaria de convidar para um jantar meus ' + guests[1] + '.')
print('Gostaria de convidar para um jantar meus ' + guests[2] + '.')

