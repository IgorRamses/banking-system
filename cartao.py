import random

def numero():
    primeiro_bloco = random.randint (1000, 9999)
    segundo_bloco = random.randint (1000, 9999)
    terceiro_bloco = random.randint (1000, 9999)
    quarto_bloco = random.randint (1000, 9999)

    numero_t = (f'{primeiro_bloco} {segundo_bloco} {terceiro_bloco} {quarto_bloco}')
    print(numero_t)
    

def cvc():
    primeiro_numero = random.randint (1, 9)
    segundo_numero = random.randint (1, 9)
    terceiro_numero = random.randint (1, 9)

    c_v_c = (f'{primeiro_numero}{segundo_numero}{terceiro_numero}')
    print(c_v_c)

def bandeiras():
    bandeiras = ['Visa', 'MasterCard', 'Elo', 'Hibercard', 'American Express']
    bandeira = random.choice(bandeiras)
    print(bandeira)