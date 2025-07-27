fila = []

def adicionar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    fila.append(nome)
    print(f"{nome} entrou na fila.")

def atender_pessoa():
    if not fila:
        print("A fila está vazia. Nenhuma pessoa para atender.")
        return

    lote = 99
    atendidos = []
    for _ in range(lote):
        if fila:
            pessoa = fila.pop(0)
            atendidos.append(pessoa)
            print(f"{pessoa} foi atendido.")
        else:
            print("A fila está vazia. Nenhuma pessoa para atender.")
            break
    if atendidos:
        print(f"Pessoas atendidas: {atendidos}")

def mostrar_fila():
    if fila:
        print("Fila atual:")
        for i, pessoa in enumerate(fila, start=1):
            print(f"{i}. {pessoa}")
    else:
        print("Fila vazia.")

def menu():
    while True:
        print("\n=== Fila de Atendimento ===")
        print("1. Adicionar pessoa")
        print("2. Atender pessoas")
        print("3. Mostrar fila")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_pessoa()
        elif opcao == "2":
            atender_pessoa()
        elif opcao == "3":
            mostrar_fila()
        elif opcao == "4":
            print("Encerrando o simulador de fila.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
