def subtracao (a, b ):
    return a - b


def adicao (a, b ):
    return a + b


def multiplicacao (a, b):
    return a * b


def divisao (a, b) :
    if b != 0:
        return a / b
    return "Não é possível dividir por zero"


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))



print('Somar: ' , adicao(n1 , n2))
print('Subtrair: ' , subtracao(n1 , n2))
print('Multiplicar: ' , multiplicacao(n1 , n2))
print('divisao: ' , divisao(n1 , n2))