guests = ['amigos', 'familiares', 'inimigos']
guests.insert(0,'melhores amigos')
guests.insert(1,'conhecidos')
guests.insert(2,'irmãos da igreja')
guests.append('amigos da faculdade')

sorry = ' sinto muito, mas convido você no próximo jantar.'

print('Aconteceu um emprevisto e só posso convidar algumas pessoas para o jantar.')
print('-----------')
print(guests.pop(-1).title() + sorry)
print(guests.pop(5).title() + sorry)
print(guests.pop(3).title() + sorry)
print(guests.pop(2).title() + sorry)
print(guests.pop(1).title() + sorry)
print('-----------')
print(guests[0].title() +', conto com a presença de vocês!')
print(guests[1].title() +', conto com a presença de vocês!')
print('-----------')
#O método pop() remove o último item de uma lista, mas permite que
#você trabalhe com esse item depois da remoção.

del guests[0]
del guests[0]
#removendo elementos de uma lista
print('Número de convidados confirmado é:', guests)