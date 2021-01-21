num1 = int(input())
resposta = ''

if(num1%2 == 0):
    resposta += f'{num1} é par'

    if num1%4 == 0:
        resposta += f' e divisivel por 4.'
else: resposta += f'O número {num1} é impar.'

print(resposta)