print('Digite "quit" para sair!')
print('-----------------------')
while True:
    inp_ingred = input('Digite alguns ingredientes que você precisa para fazer sua pizza: ')
    
    if inp_ingred == 'quit':
        break
    else:
        print('Você adicionou ' + inp_ingred + ',' \
                + ' à sua lista de ingredientes!')
    
    more_ingred = input('\nDeseja adicionar mais algum igrediente?' \
                                             + ' Sim ou não? ')
    
    if more_ingred.lower() == 'sim':
        inp_more = input('Qual igrediente deseja adicionar? ')
        print('Você adicionou ' + inp_ingred + ', ' + inp_more + \
                                    ' à sua lista de ingredientes!')
    elif more_ingred == 'não':
        break
    elif more_ingred != 'Sim ou não':
        print('Você precisa digitar "sim" ou "não".' + more_ingred) #preciso que retorne a pergunta
    elif more_ingred == 'quit':
        break
           


        






