def divisores(num):
    div = []  #lista de divisores
    c = 1  #contador
    while c <= num:
        if num % c == 0:
            div.append(c)
        c+=1
    return div

numero = int(input("Número:  "))

imprimir = divisores(numero)

print(f'O número {numero} possui {len(imprimir)} divisores: {imprimir}')