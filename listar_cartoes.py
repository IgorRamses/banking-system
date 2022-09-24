import time

cartoes_cadastrados = [1,2,3,4,5,6]
print('Seja bem vindo')
time.sleep(1)
print('Todos os seus cartões:')
time.sleep(1)
print()
print(cartoes_cadastrados) # PRÉ-VISUALIZAÇÃO DE TODOS OS CARTÕES JÁ CADASTRADOS
print() #ABAIXO DE CADA IMAGEM DE CARTÃO CONTÉM UM BOTÃO DESTINADO A EXCLUSÃO DOS CARTÕES
#O CLINTE AO CLICAR NO BOTÃO DE EXCLUIR CARTÃO, APARECE DUAS OPÇÕES:
print('[E]xcluir cartão') #EXCLUI O CARTÃO ESCOLHIDO DO PERFIL DO USUÁRIO
print('[C]ancelar') #CANCELA A OPERAÇÃO

decision_delete = input()

if decision_delete == 'E' or decision_delete == 'e':
    pass #AO CLICAR PRA EXCLUIR O CARTÃO, O SISTEMA DELE O CARTÃO AUTOMATICAMENTE
elif decision_delete == 'C' or decision_delete == 'c':
    pass # AO CLICAR NESSA OPÇÃO, CANCELARÁ A OPÇÃO DE EXCLUSÃO DE CARTÃO
else:
    pass

import tela_inicial_cliente