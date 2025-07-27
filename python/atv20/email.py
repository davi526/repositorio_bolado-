def verificar_email(email):
    if "@" not in email or "." not in email:
        return False
    partes_email = email.split("@")
    if len(partes_email) != 2:
        return False
    usuario, dominio = partes_email
    if not usuario or not dominio:
        return False
    if "." not in dominio:
        return False
    return True

email = input("Digite seu email: ")
if verificar_email(email):
    print("Email válido.")
else:
    print("Email inválido.")