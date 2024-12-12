from catalogo.produto import Produto
import logging

# Configuração básica do logger para capturar logs 
logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Obtém um logger específico para este módulo
logger = logging.getLogger(__name__)

class Pedido:
    # Inicializa o pedido com um cliente e uma lista de produtos
    def __init__(self, cliente: str):
        self.produtos = []
        self.cliente = cliente
        logger.info(f"Pedido criado para o cliente {cliente}.")
    
    def adicionarProduto(self, produto: Produto):
        try:
            # Verifica se o produto já foi adicionado ao pedido
            if any(p.id == produto.id for p in self.produtos):
                raise ValueError(f"Produto com ID {produto.id} já existe.")
            
            # Adiciona o produto ao pedido
            self.produtos.append(produto)
            logger.info(f"Produto {produto.nome} adicionado ao pedido com ID {produto.id}.")
        
        # Registra qualquer erro ao adicionar o produto
        except Exception as e:
            logger.error(f"Erro ao adicionar produto {produto.nome}: {e}")

    def calcularTotal(self):
        try:
            # Calcula o valor total dos produtos no pedido
            total = sum(produto.preco for produto in self.produtos)
            
            # Aplica um desconto de 10% se o total for maior que 100
            if total > 100:
                desconto = total * 0.10
                total -= desconto
                logger.info(f"Desconto de 10% aplicado ao pedido de {self.cliente}. Total com desconto: R${total:.2f}.")
            else:
                logger.info(f"Total do pedido de {self.cliente}: R${total:.2f}. Sem desconto aplicado.")
            
            return total
        
        # Registra qualquer erro ao calcular o total
        except Exception as e:
            logger.error(f"Erro ao calcular o total do pedido de {self.cliente}: {e}")
            return 0.0
