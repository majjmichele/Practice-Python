from random import randint 

numero = randint(0, 1000)  #sorteio de um número aleatório

qtd = len(str(numero))  #quantidade de casas decimais

while True:
    pergunta = int(input(f'O número tem {qtd} casas decimais e esta entre 0 e 1000:  '))

    if pergunta > numero:
        print('Muito altooooo!')
    elif pergunta < numero:
        print('Muito baixooooo!')
    else:
        print('Acertooooooooouuuuuuuuuuuuuuuuuuu!')
        break
