valor_carro = float(input('Valor pago no automóvel: '))
valor_investido = float (input ('Valor investido: '))
valor_venda = float (input('Valor de venda: '))

valor_custo = valor_carro + valor_investido 

valor_lucro = valor_venda - valor_custo

print('=================================')
print (f'Custo total R${valor_custo}')
print('=================================')
print (f'Lucro obtido R${valor_lucro}')
print('=================================')

if valor_lucro > 0 :
    print('Resultado: Lucro na venda! ')
elif valor_lucro < 0:
    print ('Resultado: Sem lucro. Prejuizo')
else : 
    print ('Empate')