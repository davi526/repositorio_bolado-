def numero_para_binario():
    binario = ""
    numero = int(input ("Digite um número inteiro: "))
    if numero == 0:
        return "0"
    while numero > 0:
        resto = numero % 2 
        binario = str(resto) + binario
        numero = numero // 2 
    return binario
print(numero_para_binario()) 
                 