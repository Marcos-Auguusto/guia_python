#requestedToppings = ['mushrooms', 'green peppers','extra cheese']

#for requestedTopping in requestedToppings:   
#    if requestedTopping == 'green peppers':
#        print('Sorry, we are out of green peppers right now.')
#    else:
#        print( 'Adding' + requestedTopping + '.')

#print('\nFinished making your pizza!')

#requestedToppings = ['Green peppers']

#if requestedToppings:
#    for requestedTopping in requestedToppings:
#        print('Adding ' + requestedTopping + '.')
#        print('\nFinished making your pizza!')
#else:
#    print('Are you sure you want a plain pizza?')

avaliableToppings = ['musshrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requestedToppings = ['musshrooms', 'french fries', 'extra cheese']

if requestedToppings:
    for requestedTopping in requestedToppings:
        if requestedTopping in avaliableToppings:    
            print('Adding ' + requestedTopping + '.')
            print('\nFinished making your pizza!')
        else:
            print("Sorry, we don't have" + requestedTopping + '.')
else:
    print('Are you sure you want a plain pizza?')
