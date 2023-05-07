userLogin = ['admin']

if userLogin:
    for usersLogin in userLogin:
        if usersLogin == 'admin':
            print('Olá admin, gostaria de ver um relatório de status?')
        elif usersLogin == 'dentista':
            print('Olá dentista, gostaria de ver os horários agendados para hoje?')
        elif usersLogin == 'psicologo':
            print('Olá psicologo, gostaria de ver os horários agendados para hoje?')
        elif usersLogin == 'neurocirurgião':
            print('Olá neurocirurgião, gostaria de ver os horários agendados para hoje?')
        elif usersLogin == 'paciente':
            print('Olá paciente, gostaria de saber o horário e o dia agendado para a sua consulta?')
        else:
            print('Você não está cadastrado em nosso banco de dados, tente fazer o login novamemte')
            secLogin = input('Digite a sua função: ')
else:
    print('Você não está cadastrado em nosso banco de dados, tente fazer o login novamemte')
    secLogin = input('Digite a sua função: ')