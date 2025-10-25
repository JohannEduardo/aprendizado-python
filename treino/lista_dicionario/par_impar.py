#CRIAR UM SISTEMA QUE RECEBA 10 NUMEROS E ARMAZENE ELES NA LISTA, SEPARA EM DUAS LISTAS PAR E IMPAR


lista_todos_numeros = [ ]
lista_impares = [ ]
lista_pares = [ ]
for i in range (10):
    numero_escolhidos = int(input('Escolha 10 números: '))
    lista_todos_numeros.append(numero_escolhidos)
    if numero_escolhidos % 2 == 0:
        lista_pares.append(numero_escolhidos)
    else:
        lista_impares.append(numero_escolhidos)
    
print (f'{lista_todos_numeros}  Todos os numeros')
print (f'{lista_impares}  Todos os Impares')
print (f'{lista_pares}  Todos os Pares')