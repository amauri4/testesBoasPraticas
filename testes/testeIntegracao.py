import unittest
from unittest.mock import patch
from catalogo.produto import Produto
from catalogo.catalogo import Catalogo
from pedidos.pedido import Pedido

class TestIntegracao(unittest.TestCase):

    def setUp(self):
        self.catalogo = Catalogo()
        self.produto1 = Produto(1, "Camiseta", 50.0)
        self.produto2 = Produto(2, "Tênis", 120.0)
        self.catalogo.adicionarProduto(self.produto1)
        self.catalogo.adicionarProduto(self.produto2)
        self.pedido = Pedido("João Silva")

    def test_integracao_pedido_sem_desconto(self):
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(1))
        total = self.pedido.calcularTotal()
        self.assertEqual(total, 50.0)  

    def test_integracao_pedido_com_desconto(self):
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(1))
        self.pedido.adicionarProduto(self.catalogo.buscarProduto(2))
        total = self.pedido.calcularTotal()
        self.assertEqual(total, 153.0) 

if __name__ == "__main__":
    unittest.main()
