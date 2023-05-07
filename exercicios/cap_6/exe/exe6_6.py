favorite_languages = {
    'jen':'python', 'sarah':'c', 'edward':'', 'phil':'python', }

favorite_languages['joão'] = ''
favorite_languages['jean'] = 'java scripts'
respond = ['phil', 'sarah', 'jen', 'jean']

for respond_languages in favorite_languages.keys():
    if respond_languages in respond:
        print("Thanks for answering the questions, " + respond_languages.title())