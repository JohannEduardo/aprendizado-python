# 'CHAVE' : 'VALOR'

meu_dicio = {'nome': 'Felipe', 'idade': 25, 'profissao' : 'Dev'}

print(meu_dicio['nome'])

meu_dicio.get('profissao', {}) #FORMA MAIS EXATA DE PUXAR, ELE FAZ A VERIFICAÇÃO EXTRA E RETORNA NONE SE N EXISTIR A CHAVE

meu_dicio.pop('idade') #REMOVER CHAVE

meu_dicio.keys() #RETORNA AS CHAVES DISPONIVEOS DENTRO DO DICIONARIO

meu_dicio.values() #RETORNA OS VALORES DAS CHAVES DENTRO DO DICIONARIO

meu_dicio.clear() #LIMPA OS VALORES DO DICIONARIO

meu_dicio.copy() #CRIA COPIA 

# PARTICULARIDADES

pessoa = {
    'nome' : 'Felipe',
    'idade': 25,
    'profissao' : 'Dev',
    'interesses' : ['Python', 'Programação', 'Notebooks'],
    'pet' : {
        'nome': 'Loki',
        'idade' : 1,
        'peso' : '2kg'
    } 
}

pessoa.get('nome')

pessoa.get('interesses')

pessoa.get('interesses')[0]

pessoa.get('pet').get('nome')

#ADICIONAR VALOR DEPOIS DE CRIADO O DICIONARIO

pessoa['ano_nascimento'] = 1997

for chave in pessoa:
    print(chave)