def palidromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

palabra = input("digite uma palavra:")
if palidromo(palabra):
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")




# DAORA ESSE BAGUI DE INVERER ::-1 SLK 