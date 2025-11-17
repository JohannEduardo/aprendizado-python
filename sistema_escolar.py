lista_aluno = []
lista_professor = []
lista_turma = []


def sub_opcao():  # FUNÇÃO CRIADA PARA FICAR MAIS FACIL A CHAMADA
    sub_opcao_escolha = int(
        input(
            """
    ===== SUB MENU =====
        1 . Adicionar. 
        2 . Listar.
        3 . Atualizar.
        4 . Excluir.
        9 . Voltar ao menu principal 
                              
                              
        Digite a opção desejada: """
        )
    )

    return sub_opcao_escolha


while True:
    opcao_escolha = int(
        input(
            """

    ===== MENU =====
        1 . Gerenciar estudantes.
        2 . Gerenciar professores.
        3 . Gerenciar turmas.
        9 . SAIR
        
        Escolha a opção desejada: """
        )
    )

    if opcao_escolha == 9:
        print("Encerrando o sistema...")
        break

    if opcao_escolha == 1:
        while True:
            opcao_sub = sub_opcao()
            if opcao_sub == 9:
                print("Encerrando o submenu...")
                break
            if opcao_sub == 1:
                nome_aluno = input("DIgite seu nome: ")
                lista_aluno.append(nome_aluno)
            elif opcao_sub == 2:
                print(""" \n ====== NOMES LISTADOS ======= \n """)
                print(lista_aluno)
            elif opcao_sub == 3:
                print("Analise a lista: ")
                print(lista_aluno)
                if not lista_aluno:
                    print("\n Lista vazia, não ha nada a ser mostrado \n")
                else: 
                    print('\n Agora que você tem a lista, altere o que for necessário! \n')
                    nome_antigo = input('DIgite o nome que você deseja alterar: ')

                    if nome_antigo not in lista_aluno:
                        print('Esse nome não existe na lista')
                    else:
                        novo_nome = input('Digite o novo nome que você deseja: ')
                        indice = lista_aluno.index(nome_antigo)
                        lista_aluno[indice] = novo_nome
                    
