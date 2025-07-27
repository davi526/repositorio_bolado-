#sistema de tarefas com adicionar, listar, remover.
#achei bem chato
def add_tarefa(tarefas):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def list_tarefas(tarefas):
    if tarefas:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa encontrada.")

def rmov_tarefas(tarefas):
    if tarefas:
        list_tarefas(tarefas)
        try:
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    else:
        print("Nenhuma tarefa para remover.")
tarefas = []
while True:
    print("\nMenu:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        add_tarefa(tarefas)
    elif escolha == '2':
        list_tarefas(tarefas)
    elif escolha == '3':
        rmov_tarefas(tarefas)
    elif escolha == '4':
        print("Saindo do sistema de tarefas.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")

