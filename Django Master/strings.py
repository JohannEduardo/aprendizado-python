texto = "Aula Pycode"


print(len(texto)) #Serve para contar caracteres

print(texto.count('A')) #Quantas vezes aparece esse caracter no meu código

print(texto.find('Aula')) #Posição em que ela começa

print(texto.upper())

print(texto.lower())

print(texto.capitalize()) #Somente a primeira fica maiuscula

print(texto.title())  #Primeiras letras de uma palavra ficam maiusculas

print(texto.split()) #Retorna em listas palavras do nosso texto

lista_de_palavras = texto.split()
'-'.join(lista_de_palavras)

print(texto.strip())  #Corta espaços em branco
