glossary_word = {
    'if':'se','else':'senão', 'list':'lista', 'print':'imprimir', 'method':'método'}
for glossary_words in glossary_word:
    if glossary_words == 'if':
        print('If significa:'), print(glossary_word['if']), print('\n')
    elif glossary_words == 'else':
        print('Else significa:'), print(glossary_word['else']), print('\n')
    elif glossary_words == 'list':
        print('List significa:'), print(glossary_word['list']), print('\n')
    elif glossary_words == 'print':
        print('Print significa:'), print(glossary_word['print']), print('\n')
    elif glossary_words == 'method':
        print('Method significa:'), print(glossary_word['method']), print('\n')
    else:
        exit()
