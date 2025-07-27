def calculadora(operacao, num1, num2):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 -num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"
    
num1 = int(input("gigite o primeiro numero: "))
num2 = int(input("gigite o segundo numero: "))
operacao = input("digite a operação (+,-,*,/): ")
resultado = calculadora(operacao, num1, num2)
print(f"O resultado da operação {num1} {operacao} {num2} é: {resultado}")




 