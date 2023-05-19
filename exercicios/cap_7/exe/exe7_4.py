lista_ingr = []

print("Escolha uma opção:")

while True:
    opcao = input("[i]nserir [a]pagar [l]istar [s]air ")
    
    if opcao == "i":
        add_item = input("Qual item você deseja adicionar? ")
        lista_ingr.append(add_item)
    elif opcao == "a":
        delet_item = input("Qual item deseja apagar? Exemplo: 1, 2...")
        int_input_del = int(delet_item)
        del lista_ingr[int_input_del]
    elif opcao == "l":
        for i, items in enumerate(lista_ingr):
            print(i, items)
    elif opcao == "s":
        break
    else:
        print("Você precisa selecionar uma opção!")
    


           


        






