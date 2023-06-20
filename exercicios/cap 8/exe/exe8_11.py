def items_sandwich(*items):
    print("\nForam acrescentado os seguintes items em seu sanduiche:")
    for item in items:
        print("- " + item)

items_sandwich("2 hamburguer")
items_sandwich("adicional de picles", "adicional bacon")
items_sandwich("milho", "mussarela", "picles", "ovos")