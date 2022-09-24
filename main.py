import time 

print('Seja bem vindo')
time.sleep(1)
print('Deseja entrar como [A]dministrador ou [C]liente ? ')
decision = input()
if decision == 'a' or decision == 'A':
    print('Deseja efetuar o cadastro ou login? [c]adaster, [l]ogin or [r]ecuperação de senha')
    choice = input()
    if choice == 'c' or choice == 'C':
        time.sleep(0.5)
        import cadastro_adm

    elif choice == 'l' or choice == 'L':
        time.sleep(0.5)
        import login_adm

    elif choice == 'r' or choice == 'R':
        time.sleep(0.5)
        import recuperar_senha

    else:
        pass

elif decision == 'c':
    print('Deseja efetuar o cadastro ou login? [c]adaster, [l]ogin or [r]ecuperação de senha')
    choice_1 = input()

    if choice_1 == 'c' or choice_1 == 'C':
        time.sleep(0.5)
        import cadastro_cliente

    elif choice_1 == 'l' or choice_1 == 'L':
        time.sleep(0.5)
        import login_cliente
        
    elif choice_1 == 'r' or choice_1 == 'R':
        time.sleep(0.5)
        import recuperar_senha

    else:
        pass
