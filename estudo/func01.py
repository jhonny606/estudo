def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [6, 3, 5, 6, 9, 8]
dobra(valores)
print(valores)