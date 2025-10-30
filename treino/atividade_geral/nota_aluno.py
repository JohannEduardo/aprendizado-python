# CRIAR UM SISTEMA QUE PEÇA A IDADE E NOTAS DO ALUNO

#Aluno digita o nome
nome_aluno = input("Digite seu nome: ")

#Nome exibido no terminal
print(f"Seja Bem-Vindo {nome_aluno}")

#Criação do diiconario, exibindo o nome do aluno. Notas e situação.
nome_dicionario = {"nome": nome_aluno, "notas": {}, "situacao": ""}

#Criação do loop e limitando até 4. Nele sera adicionado a nota dos alunos
for i in range(4):
    nota = float(input(f"Digite sua nota {i + 1}º:  "))
    nome_dicionario["notas"][f"nota {i + 1}"] = nota  #Adicionando a varivel nota dentro do dicionario notas que fica dentro de nome_dicionario
media = sum(nome_dicionario["notas"].values()) / len(nome_dicionario["notas"]) #Calculando as 4 notas e dividindo pela quantidade de notas

#Trazendo a analise condicional para definir a situação do aluno
if media > 6:
    situacao_aluno = "Aprovado"
else:
    situacao_aluno = "Reprovado"
#Declarando o resultado da variavel situação
nome_dicionario["situacao"] = situacao_aluno

#Mostra o resultado geral
print(nome_dicionario)

#Criado sistema que adiciona nome + nota + situação em python