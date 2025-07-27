def calcular_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celcius = float(input("Digite a temperatura em Celsius: "))
resultado = calcular_temperatura(celcius)
print(f"A temperatura em Fahrenheit é: {resultado}°F")

