rios = {'nilo':'egito', 'tietê':'brasil', 'jordão':'isrrael'}
rios['amazonas'] = 'brasil'

for key,values in rios.items():
    print('O rio ' + str(key.title()) + ' corre pelo ' + str(values.title()))