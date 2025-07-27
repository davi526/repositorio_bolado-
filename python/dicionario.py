contatos = {}

def add_nome(nome):
    contatos[nome] = True
    print(f"Nome '{nome}' adicionado.")

def buscar_nome():
    nome = input("Digite o nome para buscar: ")
    if nome in contatos:
        print(f"Nome encontrado: {nome}")
    else:
        print(f"Nome '{nome}' não encontrado.")

while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. buscar Contatos")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        nome = input("Digite o nome para adicionar: ")
        add_nome(nome)
    elif escolha == '2':
        buscar_nome()
    elif escolha == '3':
        print("Saindo do sistema de contatos.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
