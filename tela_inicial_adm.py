import time

print('Seja bem vindo ao NEWSYSBANK')
time.sleep(1)
print('Oferecemos 3 tipos diferentes de serviços:')
print()
print('(1) Aprovação de cartão novo ')
print('(2) Aprovação de cadastro de cartão')
print('(3) Visualização de clientes')
print('Qual serviço você necessita ?')
decision_client= input()
if decision_client == '1':
    import aprovacao_cartao
elif decision_client == '2':
    import aprovacao_cadastro_cartao
elif decision_client == '3':
    import visualizacao_clientes_adm
else:
    pass