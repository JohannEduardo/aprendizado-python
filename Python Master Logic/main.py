print ('Seja Bem-Vindo ao sistema que tras o seu Resultado: ')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))


media = ( n1 + n2 + n3 +n4 ) / 4

if media > 8.5 :
    print ('Excelente. Aprovado!')
elif media >= 6:
    print ('Aprovado.')
else: 
    print('Reprovado.')