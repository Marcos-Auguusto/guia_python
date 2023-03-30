cities = {
    'goiania':{'temperature':'quente', 'country':'brasil',},
    'sao paulo':{'temperature':'as vezes frio','country':'brasil',},
    'rio grande do sul':{'temperature':'frio','country':'brasil',},
}
cities['para'] = {'temperature':'quente', 'country':'brasil'}

for city, city_info in cities.items():
    print('\nCidade: ' + city.title())
    print('Temperatura: ' + city_info['temperature'])
    print('País: ' + city_info['country'].title())