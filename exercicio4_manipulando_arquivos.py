a = open('arquivo_teste.txt')
b = [i.split() for i in a]

indice = {}

for i in b:
    for j in i:
        if j in indice:
            indice[j] += 1
        else:
            indice[j] = 1

print(indice)