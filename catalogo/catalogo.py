import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from .produto import Produto

class Catalogo:
    def __init__(self):
        self.produtos=[]
    
    def adicionarProduto(self, produto: Produto):
        try:
            if any(p.id == produto.id for p in self.produtos):
                raise ValueError(f"Produto com ID {produto.id} já existe.")
            self.produtos.append(produto)
            logger.info(f"Produto {produto.nome} adicionado ao catálogo com ID {produto.id}.")
        except Exception as e:
            logger.error(f"Erro ao adicionar produto {produto.nome}: {e}")
    
    def listarProdutos(self):
        return self.produtos
    
    def buscarProduto(self, id: int):
        try:
            for produto in self.produtos:
                if produto.id == id:
                    return produto
            raise ValueError(f"Produto com ID {id} não encontrado.")
        except Exception as e:
            logger.error(f"Erro ao buscar produto por ID {id}: {e}")
            return None