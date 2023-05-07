person = {
    'person1':{'first_name':'josiel', 'last_name':'carvalho','age':29, 'city':'sao paulo'},
    'person2':{'first_name':'pedro', 'last_name':'churrasco', 'age':22, 'city':'sao paulo'},
    'person3':{'first_name':'eitor', 'last_name':'brandão', 'age':25, 'city':'sao paulo'}
}

for persons, persons_info in person.items():
    print('\nUsername: ' + persons)
    full_name = persons_info['first_name'] + ' ' + persons_info['last_name']
    location = persons_info['city']
    age = str(persons_info['age'])
    print('\tFull name: ' + full_name.title())
    print('\tTem ' + age + ' anos e mora em ' + location.title() + '.')   