dicionario = {'Roberta':'01/09/2000', 'Kaik':'11/05/1994', 'Anderson':'02/01/2003'}

print("Bem-vindo ao dicionário de aniversário. Nós sabemos os seguintes aniversários: ")

for x in dicionario: 
    print(x)

#while True:

print('#'*20)
pergunta = input('Deseja saber qual aniversário? ')

if pergunta in dicionario:
    print(f'{pergunta} nasceu em {dicionario[pergunta]}')
    print('#'*20)

else:
    novo = input('Registro não encontrado. Deseja adicionar? (s/n) ')
    

    if novo == 's':
        aniversario = input(f'Digite a data de aniversario de {pergunta}: ') 
        dicionario[pergunta] = aniversario
        print('#'*20)
    else:
        print('Então, bye bye.')
        print('#'*20)


'''
    basicamente o problema pede que seja criado um dicionario
    com nomes - como chaves- e a data de nascimento como 
    valores, e que o usuario quando digitar o nome
    seja impresso a data, caso contrário se o úsuario desejar 
    adiciona uma nova chave
'''