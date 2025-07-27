def votacao():
    print("bem vindo a urna eletrônica")
    print("Digite o número do candidato para votar:")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Candidato C")
    print("00 - NULO OU BRANCO")
    votos = {1: 0, 2: 0, 3: 0, 'nulo': 0}
    while True:
        voto = input("Digite seu voto (ou 'sair' para encerrar):")
        if voto == 'sair':
            break
        if voto == '1':
            votos[1] +=1
            print("Voto registrado para Candidato A")
        elif voto == '2':
            votos[2] +=1
            print("Voto registrado para Candidato B")
        elif voto == '3':
            votos[3] +=1
            print("Voto registrado para Candidato C")   
        elif voto == '00':
            votos['nulo'] +=1
            print("Voto registrado como NULO OU BRANCO")
        else:
            print("Voto inválido. Tente novamente.")
        

votacao()
print("Votação encerrada.")
