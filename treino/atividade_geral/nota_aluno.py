# CRIAR UM SISTEMA QUE PEÇA A IDADE E NOTAS DO ALUNO


nome_aluno = input("Digite seu nome: ")


print(f"Seja Bem-Vindo {nome_aluno}")

nome_dicionario = {"nome": nome_aluno, "notas": {}, "situacao": ""}


for i in range(4):
    nota = float(input(f"Digite sua nota {i + 1}º:  "))
    nome_dicionario["notas"][f"nota {i + 1}"] = nota
media = sum(nome_dicionario["notas"].values()) / len(nome_dicionario["notas"])

if media > 6:
    situacao_aluno = "Aprovado"
else:
    situacao_aluno = "Reprovado"

nome_dicionario["situacao"] = situacao_aluno


print(nome_dicionario)

#Criado sistema que adiciona nome + nota + situação em python