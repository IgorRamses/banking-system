import time

while True:

    print('Deseja cadastrar um cartão ? [y]es or [n]o')
    cart = input()
    if cart == 'y':
        print('Digite o número do cartão: ')
        number_cart = input()
        if not number_cart.isdigit():
            print('This is not a valid number')
            time.sleep( 1 )
            print('Exiting the system...')
            break
        qtd_characters_number = len(number_cart)
        while (qtd_characters_number > 16 or qtd_characters_number <16):
            print('You need to enter 3 characters. ')
            number_cart = ('Enter your number cart: ')
            qtd_characters_number = len(number_cart)
        print('Digite o CVC do cartão: ')
        cvc_cart = input()
        if not cvc_cart.isdigit():
            print('This is not a valid number')
            time.sleep( 1 )
            print('Exiting the system...')
            break
        qtd_characters_cvc = len(cvc_cart)
        while (qtd_characters_cvc > 3 or qtd_characters_cvc <1):
            print('You need to enter 3 characters. ')
            cvc_cart = ('Enter your cvc: ')
            qtd_characters_password = len(cvc_cart)
        print('Digite a data de validade do cartão: EX: XX/XX (Somente números) ')
        date_cart = input()
        print('Digite a bandeira do cartão: ')
        flag_cart = input()
        print('Digite o nome do titular do cartão ?')
        name_cart = input()
        time.sleep(1)
        print('Nome do titular:')
        print(name_cart)
        print('Número do cartão:')
        print(number_cart)
        print('CVC do cartão:')
        print(cvc_cart)
        print('Bandeira do cartão:')
        print(flag_cart)
        print('Data de validade do cartão:')
        print(date_cart)
        time.sleep(1)
        print('Confere ? [y]es or [n]o')
        opinion = input()
        if opinion == 'y':
            print('Pedido de cadastro de cartão será enviado para análise.')
            print()
            time.sleep(1)
            print('Dseja cadastrar outro cartão ? [y]es or [n]o')
            create_cart = input()
            if create_cart == 'y':
                continue
            elif create_cart == 'n':
                import tela_inicial_cliente
            else:
                break
            
        elif opinion == 'n':
            import tela_inicial_cliente

    elif cart =='n':
        pass