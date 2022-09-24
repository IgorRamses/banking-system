import time

mensagens = [1,2,3,4,5,6]
print('Mensagens de solicitação de aprovação de cadastro de cartão')
time.sleep(1)
print(mensagens) #EXEMPLO DE CAIXA DE MENSAGENS
print('[A]provar solicitação de cadastro')
print()
print('[R]eprovar solicitação de cadastro')
resposta_cadastro = input()
if resposta_cadastro == 'A' or resposta_cadastro == 'a': #SISTEMA ENVIARÁ UMA MENSAGEM PARA O CLIENTE DIZENDO: 'PARABÉNS, O CADASTRO DO SEU CARTÃO FOI APROVADO'
    import tela_inicial_adm
    import tela_inicial_adm
elif resposta_cadastro == 'R' or resposta_cadastro == 'r':
    print('Por qual motivo a solicitação de aprovação está sendo negada ?')
    motivo_reprovado = input() # A MENSAGEM ESCRITA PELO ADMINISTRADOR SERÁ ENVIADA PARA O CLIENTE
    import tela_inicial_adm
    
