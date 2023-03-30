lista = list(range(1,7))
print(lista)
print('-------------------------------------')

number = list(range(1,11))
print(number)
print('-------------------------------------')

even_numbers = list(range(2,12,2))
print(even_numbers)
print('-------------------------------------')

squares = []

for value in range(1,11):
    squares.append(value**2)
print(squares)
print('-------------------------------------')

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
print('-------------------------------------')

squares =  [value**2 for value in range(1,11)], print(squares)