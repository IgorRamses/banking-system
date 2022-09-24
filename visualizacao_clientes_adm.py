import time

estado = [1,2,3,4,5,6]
quantidade_de_cartoes = [1,2,3,4,5,6] 
ordem_alfabetica = [1,2,3,4,5,6]


print('Bem vindo a tela de visualização de clientes:')
time.sleep(0.5)
print('Visualizar clientes por [e]stado, [q]uantidade de cartões ou [o]rdem alfabética ?')
choice_1 = input()
if choice_1 == 'e':
    print(estado)
    import tela_inicial_adm
elif choice_1 == 'q':
    print(quantidade_de_cartoes)
    import tela_inicial_adm
elif choice_1 == 'o':
    print(ordem_alfabetica)
    import tela_inicial_adm
else:
    pass