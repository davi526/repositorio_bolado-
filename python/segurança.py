def login_seguranca():
    tentativas = 3
    while tentativas > 0:
        nome = input("Digite seu nome de usuário: ")
        senha_correta = input("Digite sua senha: ")
        if nome == "admin" and senha_correta == "1234":
            print("Login bem-sucedido!")
            break
        else:
            tentativas -= 1
            print("Nome de usuário ou senha incorretos.")
            if tentativas > 0:
                print(f"Tentativas restantes: {tentativas}")
            else:
                print("Número máximo de tentativas excedido. Acesso negado.")
            


login_seguranca()    
          

            
      

       

        


