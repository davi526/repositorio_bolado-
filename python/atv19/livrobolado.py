livros = {}

def cadastrar_livro(nome, nome_autor):
    livros[nome] = nome_autor
    print(f"Livro '{nome}' cadastrado com sucesso pelo o autor '{nome_autor}'.")

def buscar_autor():
    nome_autor = input("Digite o nome do outor para buscar: ")
    encontrados = [nome for nome, autor in livros.items() if autor == nome_autor]
    if  encontrados:
        print(f"titulos encontrados de: {nome_autor}")
        for nome in encontrados:
            print(f"- {nome}") 
    else:
        print(f"Nome '{nome_autor}' não encontrado.")

while True:
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. buscar autor")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        autor_nome = input("Digite o nome do autor: ")
        nome = input("Digite o nome para adicionar: ")
        cadastrar_livro(nome, autor_nome)
    elif escolha == '2':
        buscar_autor()
    elif escolha == '3':
        print("Saindo do sistema de contatos.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
