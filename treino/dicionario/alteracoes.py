pessoa = {
    'nome' : 'Johann',
    'idade': 19,
    'peso' : 83,
    'profissao' : 'Dev'
}

print(pessoa.get('nome'))

pessoa['mae'] = 'Marilda'

print(pessoa.get('mae'))

pessoa.pop('profissao')

print(pessoa)

