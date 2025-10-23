# Criar um sistema de adivinhacao com laços de repeticao


numero_secreto = 92
tentativas = 0

numero_escolhido = int(input("Digite o número que você quer escolher (apenas inteiros): "))
tentativas += 1


while numero_escolhido != numero_secreto:
    if numero_escolhido < 50:
        print("Frio. Tente novamente.")
    elif numero_escolhido > 50 and numero_escolhido <= 70:
        print("Morno. Tente novamente.")
    elif numero_escolhido > 70 and numero_escolhido < 92:
        print("Quente. Tente novamente.")
    else:
        print(f"Você acertou. Parabens. O número era: {numero_secreto}")

    numero_escolhido = int(input("Digite outro número: "))
    tentativas += 1
    
print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")