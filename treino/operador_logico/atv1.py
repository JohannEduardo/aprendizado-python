#Criar um sistema que pega a nota mais frequencia do aluno e retorna se ele foi aprovado ou não


#CONDICIONAL E OEPRADOR LOGICO

frequencia = float(input("Em media qual sua frequencia: "))

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
n4 = float(input("Digite sua quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4 


if media >= 6 and frequencia >= 75 :
    print('Aprovado. Parabéns!')
else : 
    print('Reprovado.')