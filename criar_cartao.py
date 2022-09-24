import time
from cartao import numero, cvc, bandeiras

print('Deseja criar um cartão ? [y]es or [n]o')
choice = input()
if choice == 'y':
        print('Confirme seu nome completo:')
        nome =input()
        print('Que tipo de cartão você deseja criar ? [c]rédito, [d]ébito ou [p]oupança ?')
        print('Mas também temos os cartões multifuncionais, são eles :')
        print('[cr]édito e débito e [po]upança e débito')
        print('Qual cartão você prefere ?')
        choice_1 = input()
        if choice_1 == 'c':
            print('Temos quatro opções de data máxima de validade possível, são elas:')
            print('[2] anos de validade, '
            '[4] anos de validade, '
            '[5] anos de validade, ' 
            '[6] anos de validade.'
            )
            choice_validade = input()
            if choice_validade =='2':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2024')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente
            
            elif choice_validade =='4':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2026')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='5':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2027')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='6':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2028')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

        elif choice_1 == 'd':
            print('Temos quatro opções de data máxima de validade possível, são elas:')
            time.sleep(0.5)
            print('[2] anos de validade, '
            '[4] anos de validade, '
            '[5] anos de validade, ' 
            '[6] anos de validade.'
            )
            choice_validade = input()
            if choice_validade =='2':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2024')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente
            
            elif choice_validade =='4':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2026')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente


            elif choice_validade =='5':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2027')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='6':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2028')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

        elif choice_1 == 'p':
            print('Temos quatro opções de data máxima de validade possível, são elas:')
            time.sleep(0.5)
            print('[2] anos de validade, '
            '[4] anos de validade, '
            '[5] anos de validade, ' 
            '[6] anos de validade.'
            )
            choice_validade = input()
            if choice_validade =='2':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2024')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente
          
            elif choice_validade =='4':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2026')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='5':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2027')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='6':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2028')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente
       
        elif choice_1 == 'cr':
            print('Temos quatro opções de data máxima de validade possível, são elas:')
            time.sleep(0.5)
            print('[2] anos de validade, '
            '[4] anos de validade, '
            '[5] anos de validade, ' 
            '[6] anos de validade.'
            )
            choice_validade = input()
            if choice_validade =='2':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2024')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente
            
            elif choice_validade =='4':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2026')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='5':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2027')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='6':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2028')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente
       
        elif choice_1 == 'po':
            print('Temos quatro opções de data máxima de validade possível, são elas:')
            time.sleep(0.5)
            print('[2] anos de validade, '
            '[4] anos de validade, '
            '[5] anos de validade, ' 
            '[6] anos de validade.'
            )
            choice_validade = input()
            if choice_validade =='2':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2024')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente
            
            elif choice_validade =='4':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2026')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='5':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2027')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

            elif choice_validade =='6':
                print('Um instante, o seu cartão está sendo criado.')
                time.sleep(0.5)
                print(f'Nome:')
                print(nome)
                print('Número do cartão:')
                numero()
                print('CVC :')
                cvc()
                print('Bandeira:')
                bandeiras()
                print('Data de validade:')
                print('24/09/2028')
                print('Pedido de cartão novo será enviado para análise.')
                import tela_inicial_cliente

elif choice == 'n':
    pass