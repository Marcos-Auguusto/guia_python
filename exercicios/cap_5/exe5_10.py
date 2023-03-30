currentUsers = ['marcos', 'josiel', 'lucas', 'ricardo' ]
newUsers = ['pedro', 'eitor', 'josiel']

for newUser in newUsers:
    if newUser.lower() in currentUsers:
        print('Este nome de usuário', newUser.title() ,'já está em uso!')
    else:
        print('Nome de usuário disponivel!')
