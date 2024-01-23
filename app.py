print('\n')
print('Bem Vindo à sua lista de tarefas')

tarefas = list()

opcao = 0
while opcao != 4:
    print('''
    Escolha uma das opções abaixo:

    [1] Adicionar nova tarefa
    [2] Listar todas as tarefas
    [3] Remover tarefas 
    [4] Sair do programa
          ''')
    opcao = int(input('Qual sua opção? '))

    if opcao == 1:
        print('\n')
        tarefas.append(input('Escreva sua tarefa: '))
        print('\n TAREFA ADICIONADA')

    elif opcao == 2:
        print('\nEssa é sua lista de tarefas:')
        for c, v in enumerate(tarefas):
            print(f'Item [{c}] Tarefa: {v}' )

    elif opcao == 3:
        print('\n')
        for c, v in enumerate(tarefas):
            print(f'Item [{c}] Tarefa: {v}')
        print('\n')
        remocao = int(input('Qual o NÚMERO do item da sua lista de tarefas que voce quer remover? '))
        if remocao >= 0 and remocao < len(tarefas):
            del tarefas[remocao]
            print('Item removido com sucesso!')
        else:
            print('\nERRO: A POSIÇÃO', remocao ,'NÃO EXISTE')

    else:

        print('\n NÚMERO INVÁLIDO') 
 

print('Fim da Lista de tarefas!')

