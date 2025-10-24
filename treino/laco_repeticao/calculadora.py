#construir uma calculadora que o usuario insere um numero e retorne esse numero para ele ate 10x

numero = int(input("Digite um número inteiro para realizar a tabuada até 10x: "))

i = 1

for i in range (11):
    print(f'{numero} x {i} = {numero * i}')