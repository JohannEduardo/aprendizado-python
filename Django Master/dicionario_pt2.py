pessoa = { 'nome': 'johann', 'idade' : 19 }

pessoa['telefone'] = 987665281

##print (pessoa)

# dic aninhado



pessoa = { 'johanneduardo18@gmail.com' : {'nome': 'johann', 'idade' : 19},
           'johanneduardo19@gmail.com' : {'nome': 'johann', 'idade' : 19},
           'johanneduardo20@gmail.com' : {'nome': 'johann', 'idade' : 19},
           'johanneduardo21@gmail.com' : {'nome': 'johann', 'idade' : 19} }

##print (pessoa['johanneduardo18@gmail.com']['nome'])

for chave, valor in pessoa.items():
    print(chave, valor)

pessoa.clear() #limpa lista

pessoa.copy() # cria outra lista

pessoa.get() # ter certeza se encontra a chave, se n encontrar volte esse valor

pessoa.item() # retorna lista de tuplas

pessoa.keys () #retorna as chaves

pessoa.setdefault() # se existir mantem, se nao existir cria

pessoa.update() #atualiza e se exitir muda ####CUIDAR###

pessoa.values() #retorna todos os valores 

del pessoa['johanneduardo20@gmail.com']['idade']