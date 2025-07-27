def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

def contar_caracteres(frase):
    return len(frase)

frase = input("Digite uma frase: ")
resultado = contar_palavras(frase)
resultado_caracteres = contar_caracteres(frase)
print(f"A frase contém {resultado} palavras.")
print(f"a frase contem {resultado_caracteres} caracteres.")


