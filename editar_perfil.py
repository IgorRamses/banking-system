import time

print('EDITAR PERFIL')
time.sleep(1)
print()
print('(1) Alterar foto do perfil')
print()
print('(2) Mudar senha')
print()
print('(3) Apagar conta')
print()
print('Qual serviço você necessita ?')
decision_client_perfil = input()

if decision_client_perfil == '1':
    #CLIENTE ENTRA E VERIFICA O BOTÃO DE UPLOAD DE FOTO
    print('Upload de foto !!! (Somente arquivos .jpeg e .jpg)')
    #CLIENTE SELECIONA A FOTO
    print('Redimensionar foto')
    #CLIENTE REDIMENSIONA A FOTO
    print('Trocar foto de perfil')
    #CLINTE CLICA NO BOTÃO E A FOTO É ALTERADA
elif decision_client_perfil == '2':
    #CLINTE VER 3 CAMPOS VAZIOS
    print('Senha atual do usuário:')
    senha_atual = input()
    #INSERE A SENHA ATUAL NO CAMPO DESTINADO A ISSO
    print('Nova senha do usuário:')
    nova_senha = input()
    #INSERE A SENHA DESEJADA NO CAMPO
    print('Confirme sua nova senha:')
    confirme_nova_senha = input()
    #REPETE A NOVA SENHA NO CAMPO 
    print('Nova senha alterada')
elif decision_client_perfil == '3':
    print('Apagar conta')
    #AO CLICAR NESSA OPÇÃO APARECERÁ DUAS OPÇÕES NA TELA
    time.sleep(1)
    print('O que você deseja fazer ?')
    time.sleep(1)
    print('[A]pagar conta')
    print('[C]ancelar')
    delete_perfil = input()
    if delete_perfil == 'A'or delete_perfil == 'a':
        print('Por qual motivo deseja excluir sua conta ?')
        print()
        print('[N]ão desejo mais utilizar esse sistema')
        print('[E]stou insatisfeito com esse sistema')
        print('[I]rei migrar para outro sistema bancário')
        print('[O]utros: _______________________________')
        motivo_delete = input()
        if motivo_delete == 'N' or motivo_delete == 'n':
            print('Obrigado pelo feedback') #A CONTA SERÁ DELETADA APÓS ESSA MENSAGEM
            import main
        elif motivo_delete == 'E' or motivo_delete == 'e':
            print('Obrigado pelo feedback') #A CONTA SERÁ DELETADA APÓS ESSA MENSAGEM
            import main
        elif motivo_delete == 'I' or motivo_delete == 'i':
            print('Obrigado pelo feedback') #A CONTA SERÁ DELETADA APÓS ESSA MENSAGEM
            import main
        elif motivo_delete == 'O' or motivo_delete == 'o':
            print('Qual seria esse motivo ?')
            motivo = input()
            print('Obrigado pelo feedback') #A CONTA SERÁ DELETADA APÓS ESSA MENSAGEM
            import main
        else: 
            pass
    elif delete_perfil == 'C'or delete_perfil == 'c':
        pass
else: 
    pass