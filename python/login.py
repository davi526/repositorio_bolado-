def login(nome, senha):
    if nome == "admin" and senha == "1234":
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

nome = input("digite seu nome de usuario: ")
senha = input("digite sua senha: ")
login(nome, senha)
