usuarios = []

def criar_usuario(nome):
    usuarios.append(nome)
    print(f"Usuário {nome} criado")

def ler_usuarios():
    if usuarios:
        print("Usuários:")
        for usuario in usuarios:
            print(usuario)
    else:
        print("nao e nehum usuario -_- ")

criar_usuario("Antonio")
ler_usuarios()
criar_usuario("Jonathan mestre supremo")
ler_usuarios()
criar_usuario("Cleberton")
ler_usuarios()
