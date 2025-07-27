def caixa_eletronico(saldo, valor_saque):
    valor_notas = [100, 50, 20, 10, 5, 2, 1]
    if valor_saque > saldo:
        print("Saldo insuficiente.")
        return saldo
    if valor_saque <= 0:
        print("Valor de saque inválido.")
        return saldo

    total = valor_saque
    notas_entregues = {}

    for nota in valor_notas:
        if total >= nota:
            qtd = total // nota
            notas_entregues[nota] = qtd
            total -= nota * qtd

    if total != 0:
        print("Não foi possível realizar o saque com as notas disponíveis.")
        return saldo

    print("Saque realizado com sucesso.")
    print("Notas entregues:")
    for nota, qtd in notas_entregues.items():
        if qtd > 0:
            print(f"{qtd} nota(s) de {nota}")

    saldo -= valor_saque
    return saldo

def verificar_saldo(saldo):
    print(f"Saldo atual: {saldo}")
    return saldo

saldo = 1000

while True:
    print("\nMenu:")
    print("1. Sacar dinheiro")
    print("2. Verificar saldo")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        try:
            valor = int(input("Digite o valor do saque: "))
            saldo = caixa_eletronico(saldo, valor)
        except ValueError:
            print("Digite um número válido.")
    elif escolha == '2':
        verificar_saldo(saldo)
    elif escolha == '3':
        print("Saindo do sistema de caixa eletrônico.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
