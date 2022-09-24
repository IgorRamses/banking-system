import time


print('Bem vindo a tela de recuperação de senha:')
time.sleep(0.5)
print('Digite seu e-mail:')
email = input()
print('Insira seu nome completo:')
nome = input()
print('Digite seu CPF:')
cpf = input()
if not cpf.isdigit():
        print('This is not a valid number')
        time.sleep( 1 )
        print('Exiting ...')
        pass

print('Será enviado uma mensagem com a sua senha atual para o seu e-mail.')
import main
