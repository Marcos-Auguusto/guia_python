pizzaFav = ['Portuguesa', 'Frango c/ catupiry', '3 queijos', 'Margarita', 'Calabresa']
friendsPizza = pizzaFav[:]

pizzaFav.append('Do cliente')
friendsPizza.append('Da casa')

for allPizza in pizzaFav:
    pizzaFav = allPizza
    print('Minhas pizzas favoritas é:')
    print(pizzaFav)

print('---------------------')

for allPizzaF in friendsPizza:
    friendsPizza = allPizzaF
    print('As pizzas favoritas de meus amigos são:')
    print(friendsPizza)