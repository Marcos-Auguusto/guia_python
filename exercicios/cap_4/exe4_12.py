myFoods = ['pizza', 'falafel', 'carrot cake']
friendsFood = myFoods[:]
friendsFood.append('burguer')
myFoods.append('cookies')

for allFoods in myFoods:
    myFoods = allFoods
    print('My favorite foods are:')
    print(myFoods)

for allFoodsFriends in friendsFood:
    friendsFood = allFoodsFriends
    print("\nMy friend's favorite foods are:")
    print(friendsFood)
