#criar um sistema onde podemos controlar uma lista de compras em um hortifruti


# MENU 
def funcao_compra_hortifruti(): 
    print('[1] Adicionar Fruta')
    print('[2] Remover Fruta')
    print('[3] Lista de Frutas')
    print('[4] Sair')





sacola_compras = [ ]

while True:

    funcao_compra_hortifruti()
    escolha_usuario = int(input('Escolha uma opção: '))

    if escolha_usuario == 1:
        escolha_frutas = input('Escolha suas frutas: ')
        sacola_compras.append(escolha_frutas)
        print (sacola_compras)
    
    elif escolha_usuario == 2: 
        remover_frutas = input('Qual a fruta que você deseja retirar: ')
        sacola_compras.remover(remover_frutas)

       
    print (sacola_compras)
    
        