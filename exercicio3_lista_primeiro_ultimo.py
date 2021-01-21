def priUlt(a):
    lista_modificada = [a[0], a[len(a)-1]]
    return lista_modificada

lista = input().split()

resposta = priUlt(lista)
print(resposta)