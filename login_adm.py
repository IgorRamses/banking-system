import time
import getpass

print('Bem vindo a página de login')
time.sleep(1)
print('Insira seu CPF: (Somente números)')
cpf = input()
if not cpf.isdigit():
    print('This is not a valid number')
    time.sleep( 1 )
    print('Exiting the registration system...')
    pass
    print(' Type your password: ')
    password = getpass.getpass (' ')
    qtd_characters_password = len(password)
    while (qtd_characters_password < 8):
        print('You need to enter 8 characters.')
        password = getpass.getpass ('Enter your password: ')
        qtd_characters_password = len(password)
        print('Seja bem-vindo !!!')
        import tela_inicial_adm

print(' Type your password: ')
password = getpass.getpass (' ')
qtd_characters_password = len(password)
while (qtd_characters_password < 8):
        print('You need to enter 8 characters.')
        password = getpass.getpass ('Enter your password: ')
        qtd_characters_password = len(password)
print('Seja bem-vindo !!!')
import tela_inicial_adm
