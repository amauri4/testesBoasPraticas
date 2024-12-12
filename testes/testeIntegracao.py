import unittest
from unittest.mock import patch
from catalogo.produto import Produto
from catalogo.catalogo import Catalogo
from pedidos.pedido import Pedido

class TestIntegracao(unittest.TestCase):
    print("Iniciando testes de integração...")

    def setUp(self):
        self.catalogo = Catalogo()
        self.produto1 = Produto(1, "Camiseta", 50.0)
        self.produto2 = Produto(2, "Tênis", 120.0)
        self.produto3 = Produto(3, "Short jeans", 75.0)
        self.produto4 = Produto(4, "Cueca", 45.0)
        self.produto5 = Produto(5, "Camisa social", 299.90)
        self.produto6 = Produto(6, "Meias", 32.20)
        self.produto7 = Produto(7, "Boné", 55.0)
        self.produto8 = Produto(8, "Jaqueta de couro", 440.90)
        self.catalogo.adicionarProduto(self.produto1)
        self.catalogo.adicionarProduto(self.produto2)
        self.catalogo.adicionarProduto(self.produto3)
        self.catalogo.adicionarProduto(self.produto4)
        self.catalogo.adicionarProduto(self.produto5)
        self.catalogo.adicionarProduto(self.produto6)
        self.catalogo.adicionarProduto(self.produto7)
        self.catalogo.adicionarProduto(self.produto8)
        self.pedido = Pedido("João Silva")

    def test_integracao_pedido_sem_desconto(self):
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(1))
        total = self.pedido.calcularTotal()
        self.assertEqual(total, 50.0)  

    def test_integracao_pedido_com_desconto(self):
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(1))
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(2))
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(3))
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(4))
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(5))
        total = self.pedido.calcularTotal()
        self.assertEqual(total, 530.91) 
    
    print("Fim dos testes de integração.")
    print("\n")

if __name__ == "__main__":
    unittest.main()
