while True:
    idade = input("Quantos anos você tem? ")
    int_idade = int(idade)

    if int_idade <= 3:
        print("Igresso gratuito!")
    elif int_idade >=4 and int_idade <=12:
        print("O igresso custa R$ 10,00")
    elif int_idade >=13:
        print("O igresso custa R$ 15,00")