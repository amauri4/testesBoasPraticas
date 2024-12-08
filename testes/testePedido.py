import unittest
from unittest.mock import patch
from catalogo.produto import Produto
from pedidos.pedido import Pedido

class TestePedido(unittest.TestCase):

    def setUp(self):
        self.produto1 = Produto(1, "Camiseta", 50.0)
        self.produto2 = Produto(2, "Tênis", 120.0)
        self.pedido = Pedido("João Silva")

    @patch('pedidos.pedido.logger.info') 
    def test_adicionar_produto_com_sucesso(self, mock_info):
        self.pedido.adicionarProduto(self.produto1)
        self.assertEqual(self.pedido.produtos[0], self.produto1)
        mock_info.assert_any_call(f"Produto {self.produto1.nome} adicionado ao pedido com ID {self.produto1.id}.")
    
    @patch('pedidos.pedido.logger.info') 
    def test_calcular_total_com_desconto(self, mock_info):
        self.pedido.adicionarProduto(self.produto1)
        self.pedido.adicionarProduto(self.produto2)
        total = self.pedido.calcularTotal()
        self.assertEqual(total, 153.0)  
        mock_info.assert_any_call(f"Desconto de 10% aplicado ao pedido de João Silva. Total com desconto: R${total:.2f}.")
    
    @patch('pedidos.pedido.logger.info')  
    def test_calcular_total_sem_desconto(self, mock_info):
        self.pedido.adicionarProduto(self.produto1)
        total = self.pedido.calcularTotal()
        self.assertEqual(total, 50.0)
        mock_info.assert_any_call(f"Total do pedido de João Silva: R${total:.2f}. Sem desconto aplicado.")

if __name__ == "__main__":
    unittest.main()
