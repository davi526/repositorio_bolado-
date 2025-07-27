def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
   
    if not cpf.isdigit():
        return False
    if len(cpf) != 11:
        return False
    
    print("O CPF:", cpf)
    return True


cpf = input("Digite o seu CPF (apenas números):")
if validar_cpf(cpf):
    print("É valido.")
else: 
    print ("É invalido.")




