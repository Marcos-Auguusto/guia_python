favorites_places = {
    'person1':{'nome_pessoa':'josiel', 'first_place':'liberdade', 
    'second_place':'casa', 'third_place':'churrascaria',},
    
    'person2':{'nome_pessoa':'pedro', 'first_place':'home',
    'second_place':'liberdade', 'third_place':'clube',},

    'person3':{'nome_pessoa':'eitor', 'first_place':'bar',
    'second_place':'shopping', 'third_place':'home'},    
}
for favorite_place, place_info in favorites_places.items():
    print('\nNome: ' + place_info['nome_pessoa'].title())
    print('Lista de lugares favoritos: ' + place_info['first_place']
+ ', ' + place_info['second_place'] + ' e ' + place_info['third_place'] + '.')