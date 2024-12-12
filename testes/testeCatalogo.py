import unittest
from unittest.mock import patch
from catalogo.produto import Produto
from catalogo.catalogo import Catalogo

class TesteCatalogo(unittest.TestCase):
    print("Iniciando testes do catálogo...")

    def setUp(self):
        self.catalogo = Catalogo()
        self.produto1 = Produto(1, "Camiseta", 50.0)
        self.produto2 = Produto(2, "Tênis", 120.0)

    @patch('catalogo.catalogo.logger.info')
    def test_adicionar_produto_com_sucesso(self, mock_info):
        self.catalogo.adicionarProduto(self.produto1)
        produtos = self.catalogo.listarProdutos()
        self.assertEqual(len(produtos), 1)
        self.assertEqual(produtos[0], self.produto1)
        mock_info.assert_any_call(f"Produto {self.produto1.nome} adicionado ao catálogo com ID {self.produto1.id}.")

    @patch('catalogo.catalogo.logger.error')
    def test_adicionar_produto_duplicado(self, mock_error):
        self.catalogo.adicionarProduto(self.produto1)
        with self.assertRaises(ValueError) as context:
            self.catalogo.adicionarProduto(self.produto1)  
        self.assertEqual(str(context.exception), f"Produto com ID {self.produto1.id} já existe.")
        mock_error.assert_any_call(f"Um produto com ID '{self.produto1.id}' já existe no catálogo.")
    
    @patch('catalogo.catalogo.logger.error')
    def test_adicionar_produto_nulo(self, mock_error):
        with self.assertRaises(ValueError) as context:
            self.catalogo.adicionarProduto(None)
        self.assertEqual(str(context.exception), "O produto em questão não pode ser vazio.")
        mock_error.assert_any_call("Um produto não pode ser vazio.")
    
    def test_listar_produtos(self):
        self.catalogo.adicionarProduto(self.produto1)
        self.catalogo.adicionarProduto(self.produto2)
        produtos = self.catalogo.listarProdutos()
        self.assertEqual(len(produtos), 2)
        self.assertIn(self.produto1, produtos)
        self.assertIn(self.produto2, produtos)

    def test_buscar_produto_existente(self):
       self.catalogo.adicionarProduto(self.produto1)
       produtoBuscado = self.catalogo.buscarProduto(self.produto1.id)
       self.assertEqual(self.produto1, produtoBuscado)
    
    @patch('catalogo.catalogo.logger.error')
    def test_buscar_produto_nao_existente(self, mock_error):
        produto = self.catalogo.buscarProduto(999)
        self.assertIsNone(produto)
        mock_error.assert_any_call(f"Produto de ID 999 não encontrado.")
    
    print("Fim dos testes de catálogo.")
    print("\n")

if __name__ == "__main__":
    unittest.main()
