pet = {
    'pet1':{'tipo_animal':'cachorro', 'nome_dono':'josiel', 'info':'peludo',},
    'pet2':{'tipo_animal':'gato', 'nome_dono':'pedro','info':'careca',},
    'pet3':{'tipo_animal':'cobra', 'nome_dono':'eitor','info':'albina'}
}

for pets, pets_info in pet.items():
    print('\nPet do: ' + pets_info['nome_dono'].title())
    print('\tTipo de animal: ' + pets_info['tipo_animal'].title())
    print('\tCaracteristica do animal: ' + pets_info['info'].title())