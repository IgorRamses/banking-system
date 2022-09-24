import time

mensagens = [1,2,3,4,5,6]
print('Mensagens de solicitação de aprovação de cartão')
time.sleep(1)
print(mensagens) #EXEMPLO DE CAIXA DE MENSAGENS
print('[A]provar solicitação')
print()
print('[R]eprovar solicitação')
solicitacao = input()
if solicitacao == 'A' or solicitacao == 'a': #SISTEMA ENVIARÁ UMA MENSAGEM PARA O CLIENTE DIZENDO: 'PARABÉNS, SEU CARTÃO FOI APROVADO'
    import tela_inicial_adm
    import tela_inicial_adm
    
if solicitacao == 'R' or solicitacao == 'r':
    print('Por qual motivo a solicitação de aprovação está sendo negada ?')
    motivo_reprovado = input() # A MENSAGEM ESCRITA PELO ADMINISTRADOR SERÁ ENVIADA PARA O CLIENTE
    import tela_inicial_adm
    
