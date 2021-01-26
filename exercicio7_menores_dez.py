lista = [10,74,3,6,2,63,89,5,2,1,13,8,21,49,23]

#lista_menores = [x for x in lista if x < 10]
#print(lista_menores)

numero = int(input('Número: '))

lista_numero = [i for i in lista if i < numero]  #lista com os núeros menores que o escolhido pelo usuario
print(lista_numero)