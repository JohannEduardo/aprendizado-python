# INDICE : VALOR  INDICE SEMPRE COMEÇA EM 0

lista = []

lista.append('Marea')
lista.append('Fusca')
lista.append(10)

#APPEND SEMPRE CRIA NO FINAL DA LISTA

print(lista)

lista.copy()

lista.insert(1, 'Escort') #Adiciona elemento onde eu quiser, apenas passando o indice que ira ficar e o valor

del lista[1] # INDICE

lista.remove('Fusca') #PASSO O VALOR 

lista.count() #PUXA QUANTAS VEZES APARECE VALOR 

lista.reverse() #INVERTE VALORES DA LISTA

lista.extend() #JUNTA DUAS ARRAYS

lista.sort() #ARRUMA VALORES SEQUENCIALMENTE