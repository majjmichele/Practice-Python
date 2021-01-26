from random import randint

arquivo = open('SOWPODSdictionary.txt','r')  #Abre um arquivo .txt com sequencias de letras

arquivo = [i.rstrip() for i in arquivo]  #pega as palavras do arquivo
numero = randint(0, len(arquivo)-1)  #sorteia um numero
palavra = arquivo[numero]  # palavra recebe a valor da posição sorteada

forca = ['_' for x in palavra]  #forca recebe a quantidade de letras da palavra em _

erros = 0  #contador de erros

while True:
    letra = input('Letra:  ')

    x = 0
    while x < len(palavra):
        if (palavra[x] == letra or palavra[x].lower() == letra):  #verifica se a letra informada está na palavra sorteada
            forca[x] = letra.upper()  #troca o _ pela letra

        elif letra.upper() not in palavra: 
            erros+=1  #contador de erros
            break

        x += 1

    print(' '.join(forca))
    print(f'Você errou {erros} x')

    if '_' not in forca:  #verifica se todoas as letras foram acertadas
        print('OH MY GOSHHHHHHHHHHHHHHHHHHH, CORRECT!!!!')
        print(f'A PALAVRA ERA {palavra}')
        print("FIM DE JOGO PRO'OCÊ :)))")
        break

    elif erros == 3:
        print('NÃO FOI DESSA VEZ, MAS NÃO FIQUE TRISTE PODERIA SER BEM PIOR :))')
        print('BYE'*20)
        break



