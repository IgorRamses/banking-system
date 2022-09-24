import time

print('Seja bem vindo ao NEWSYSBANK')
time.sleep(1)
print('Oferecemos 4 tipos diferentes de serviços:')
print()
print('(1) Criar cartão')
print('(2) Cadastrar cartão')
print('(3) Listar cartões')
print('(4) Editar perfil')
print('Qual serviço você necessita ?')
decision_client= input()
if decision_client == '1':
    import criar_cartao
elif decision_client == '2':
    import cadastro_cartão
elif decision_client == '3':
    import listar_cartoes
elif decision_client == '4':
    import editar_perfil
else:
    pass