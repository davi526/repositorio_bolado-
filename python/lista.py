def conta_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

numeros = input("Digite uma lista de números separados por vírgula: ")
numeros = [int(x) for x in numeros.split(',')]
conta_lista(numeros)
print("Lista ordenada:", numeros)





