import logging

# Configuração básica do logger para capturar logs com nível INFO ou superior
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Obtém um logger específico para este módulo
logger = logging.getLogger(__name__)

from .produto import Produto

class Catalogo:
    # Inicializa a lista de produtos no catálogo
    def __init__(self):
        self.produtos = []
    
    def adicionarProduto(self, produto: Produto):
        try:
            # Verifica se o produto é válido
            if produto is None:
                logger.error("Um produto não pode ser vazio.")
                raise ValueError("O produto em questão não pode ser vazio.")
            
            # Verifica se já existe um produto com o mesmo ID
            if any(p.id == produto.id for p in self.produtos):
                logger.error(f"Um produto com ID '{produto.id}' já existe no catálogo.")
                raise ValueError(f"Produto com ID {produto.id} já existe.")
            
            # Adiciona o produto ao catálogo
            self.produtos.append(produto)
            logger.info(f"Produto {produto.nome} adicionado ao catálogo com ID {produto.id}.")
        
        # Lança o erro novamente se for um erro esperado (ValueError)
        except ValueError as ve:
            raise ve  
        
        # Registra qualquer outro erro inesperado
        except Exception as e:
            logger.error(f"Erro inesperado ao adicionar produto: {e}")
            raise e
    
    def listarProdutos(self):
        return self.produtos
    
    def buscarProduto(self, id: int):
        try:
            # Busca o produto pelo ID no catálogo
            for produto in self.produtos:
                if produto.id == id:
                    return produto
            
            # Caso o produto não seja encontrado, loga o erro
            logger.error(f"Produto de ID {id} não encontrado.")
            raise ValueError(f"Produto de ID {id} não encontrado.")
        
        # Registra erro no caso de falha na busca
        except Exception as e:
            logger.error(f"Erro ao buscar produto por ID {id}: {e}")
            return None
