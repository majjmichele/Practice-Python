#adaptação do jogo cows and bulls
from random import randint

valor = str(randint(10000, 99999))  #numero com 5 casas decimais

checagem = input('Números para checagem: ')

numeros = ''  #vai sendo atualizado conforme a verificação
contador = 0  #contador de pontos
c = 0  #contador do ciclo

while c < 5:
    if checagem[c] == valor[c]:
        numeros += valor[c]
        contador += 1
    else:
        numeros += '*'
    c+=1

print('*'*20)
print(f'Valor gerado: {valor}')
print(f'Números informados: {numeros}')
print(f'Pontos: {contador}')
print('*'*20)

'''
    O úsuario informa uma sequência numerica que se um numero coincidir 
    na mesma ordem/posição do número gerado ele ganha 1 ponto
'''