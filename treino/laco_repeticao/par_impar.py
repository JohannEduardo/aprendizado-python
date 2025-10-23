#Criar uma função que receba uma lista com numeros inteiros e diga o que e par e o que e impar


inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in inteiros:
    if i % 2 == 0:
        print(f"Pares: {i}")
    else:
        print(f"Impares: {i}")