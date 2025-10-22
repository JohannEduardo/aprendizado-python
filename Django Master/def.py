# Ao invés de ficar repetindo linhas de código, crie funções

def somar (a, b) :
    resultado = a + b
    return resultado

# return nao e obrigatorio ser declarado

# PRINT E BOM PARA APRENDIZADO, MUITAS VEZES UTILIZADOS NO INTITO DE MOSTRAR ALGO. MAS LEMBRAR SEMPRE QUE ELE E APENAS FORMA DE INTERAÇÃO COM O TERMINAL

def envia_email (nome, email):
    email = 'pycode@gmail.com'
    senha = '12345'
    nome_dest = nome
    email_dest = email
    # CONECTA PROVEDOR 
    # MONTA CORPO DO E-MAIL
    # ENVIA O EMAIL
    return f'Email enviado para: {nome_dest} com o endereço de e-mail: {email_dest}!'

pessoas = [
    {'nome': 'Johann', 'email': 'johann@gmail.com'},
    {'nome': 'Lucas', 'email': 'lucas@gmail.com'},
    {'nome': 'Juana', 'email': 'juana@gmail.com'}
]

for pessoa in pessoas:
    email_enviado = envia_email(pessoa['nome'], pessoa['email'])
    print(email_enviado)
#Nem sempre precisamos de parametros, as vezes o que precisamos pode ser encaixado dentro di bloco de codigo mesmo.