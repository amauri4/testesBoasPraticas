from catalogo.produto import Produto
from catalogo.catalogo import Catalogo
from pedidos.pedido import Pedido

# Criando o catálogo
catalogo = Catalogo()
produto1 = Produto(1, "Camiseta", 50.0)
produto2 = Produto(2, "Tênis", 120.0)
produto3 = Produto(3, "Calça moletom", 150.0)
produto4 = Produto(4, "Casaco", 209.90)

# Adicionando produtos ao catálogo
catalogo.adicionarProduto(produto1)
catalogo.adicionarProduto(produto2)
catalogo.adicionarProduto(produto3)
catalogo.adicionarProduto(produto4)

# Listando produtos
for produto in catalogo.listarProdutos():
    print(f"{produto.id}: {produto.nome} - R${produto.preco:.2f}")

# Criando um pedido
pedido = Pedido("João Silva")
produtoJoao1 = catalogo.buscarProduto(produto1.id)
produtoJoao2 = catalogo.buscarProduto(produto2.id)
produtoJoao3 = catalogo.buscarProduto(produto3.id)
produtoJoao4 = catalogo.buscarProduto(produto4.id)
pedido.adicionarProduto(produtoJoao1)
pedido.adicionarProduto(produtoJoao2)
pedido.adicionarProduto(produtoJoao3)
pedido.adicionarProduto(produtoJoao4)

# Calculando o total do pedido
print(f"Total do pedido de '{pedido.cliente}': R${pedido.calcularTotal():.2f}")
