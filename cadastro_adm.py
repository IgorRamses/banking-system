import time
import getpass

while True:

    print('Insira seu nome completo:')
    nome = input()
    print('Digite seu CPF válido: (Somente números)')
    cpf = input()
    if not cpf.isdigit():
            print('This is not a valid number')
            time.sleep( 1 )
            print('Exiting the registration system...')
            break
    else:
            pass
    print('Digite seu endereço: (Logradouro, Tipo de residência, Número)')
    endereco = input()
    print('Digite o estado no qual você reside:')
    estado = input()
    print(' Type your password: ')
    password = getpass.getpass (' ')
    qtd_characters_password = len(password)
    while (qtd_characters_password < 8):
            print('You need to enter 8 characters. ')
            password = getpass.getpass ('Enter your password: ')
            qtd_characters_password = len(password)
    print('User registered successfully')
    time.sleep(1)
    print(f'password: {password}')
    password_correct = input('Check ? [y]es ou [n]o: ')
    if password_correct == 'y':
            print(f'Be welcome, {nome}')
            time.sleep(1)
            print('Deseja fazer login no sistema ? [y]es or [n]o')
            choice = input()
            if choice == 'n':
                time.sleep( 1 )
                print('Exiting the registration system...')
                pass
            elif choice == 'y':
                import login_cliente

    elif password_correct == 'n':
            print(' Type your password: ')
            password_correct = getpass.getpass()
            qtd_characters_password = len(password_correct)
            while (qtd_characters_password < 8):
                print('You need to enter 8 characters. ')
                password_correct = getpass.getpass('Enter your password: ')
                qtd_characters_password = len(password_correct)
            print(f'Be welcome, {nome}')
            time.sleep(1)

            print('Deseja fazer login no sistema ? [y]es or [n]o')
            choice = input()

            if choice == 'n':
                time.sleep( 1 )
                print('Exiting the registration system...')
                pass
            elif choice == 'y':
                import login_adm