# Criar uma loja virtual simplificada

# ESTOQUE
# ADD PRODUTO AO CARRINHO
# CONTINUAR COMPRANDO OU SAIR
# TOTAL DA COMPRA


print("Seja Bem-Vindo ao Mercadinho!")

print("=============================================== \n")


def listaCompras():
    dicionario_itens = {
        "Maça": {"preco": 2.50, "quantidade": 10},
        "Banana": {"preco": 3.00, "quantidade": 10},
        "Morango": {"preco": 6.25, "quantidade": 10},
        "Pitanga": {"preco": 9.00, "quantidade": 10},
        "Abacaxi": {"preco": 4.32, "quantidade": 10},
        "Abacate": {"preco": 1.55, "quantidade": 10},
    }
    return dicionario_itens


estoque = listaCompras()

carrinho = { }
valor_total = 0


def mostrar_estoque():
    print("\n Produtos em Estoque \n")
    for i in estoque:
        preco = estoque[i]["preco"]
        quantidade = estoque[i]["quantidade"]
        print(f"{i} preço: {preco} quantidade: {quantidade}")


def escolha_produto():
    while True:
        mostrar_estoque()
        produto = input("Escolha seu produto: ")
        if produto in estoque:
            quantidade_desejada = int(input('Digite a quantidade desejada de itens: '))
            if quantidade_desejada < estoque[produto]['quantidade']:
                print(f'Produto adicionado no carrinho: {quantidade_desejada}x {produto}')
            else:
                print(f'Você quer adicionar uma quantidade acima da dísponivel. Quantidade dísponivel: {estoque[produto]['quantidade']}')
        else:
            print('Produto não encontrado em estoque')
        return produto, quantidade_desejada

def adicionar_carrinho():
    produto, quantidade_desejada = escolha_produto()
    carrinho[produto] = carrinho.get(produto, 0) + quantidade_desejada

    
