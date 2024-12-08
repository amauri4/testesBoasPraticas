import unittest
from unittest.mock import patch
from catalogo.produto import Produto
from catalogo.catalogo import Catalogo

class TesteCatalogo(unittest.TestCase):

    def setUp(self):
        self.catalogo = Catalogo()
        self.produto1 = Produto(1, "Camiseta", 50.0)
        self.produto2 = Produto(2, "Tênis", 120.0)

    def test_buscar_produto_por_id(self):
        self.catalogo.adicionarProduto(self.produto1)
        produto = self.catalogo.buscarProduto(self.produto1.id)
        self.assertEqual(produto.nome, "Camiseta")

    def test_listar_produtos(self):
        self.catalogo.adicionarProduto(self.produto1)
        self.catalogo.adicionarProduto(self.produto2)
        produtos = self.catalogo.listarProdutos()
        self.assertEqual(len(produtos), 2)

    @patch('catalogo.catalogo.logger.info')  # Corrigir para o caminho correto do logging
    def test_adicionar_produto_com_sucesso(self, mock_info):
        self.catalogo.adicionarProduto(self.produto1)
        listaTeste = [self.produto1]
        self.assertListEqual(self.catalogo.listarProdutos(), listaTeste)
        mock_info.assert_any_call(f"Produto {self.produto1.nome} adicionado ao catálogo com ID {self.produto1.id}.")

    @patch('catalogo.catalogo.logger.error')  
    def test_adicionar_produto_duplicado(self, mock_error):
        self.catalogo.adicionarProduto(self.produto1)
        self.catalogo.adicionarProduto(self.produto1)  
        mock_error.assert_any_call(f"Erro ao adicionar produto {self.produto1.nome}: Produto com ID {self.produto1.id} já existe.")
    
    @patch('catalogo.catalogo.logger.error')  
    def test_buscar_produto_com_erro(self, mock_error):
        produto = self.catalogo.buscarProduto(999)  
        self.assertIsNone(produto)
        mock_error.assert_any_call("Erro ao buscar produto por ID 999: Produto com ID 999 não encontrado.")
    
    @patch('catalogo.catalogo.logger.error') 
    def test_buscar_produto_com_erro_no_busca(self, mock_error):
        self.catalogo.adicionarProduto(self.produto1)
        produto = self.catalogo.buscarProduto(999)  
        self.assertIsNone(produto)
        mock_error.assert_any_call("Erro ao buscar produto por ID 999: Produto com ID 999 não encontrado.")
        
if __name__ == "__main__":
    unittest.main()
