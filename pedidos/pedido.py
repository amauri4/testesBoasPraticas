from catalogo.produto import Produto
import logging

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Pedido:
    def __init__(self, cliente: str):
        self.produtos = []
        self.cliente = cliente
        logger.info(f"Pedido criado para o cliente {cliente}.")

    
    def adicionarProduto(self, produto: Produto):
        try:
            if any(p.id == produto.id for p in self.produtos):
                raise ValueError(f"Produto com ID {produto.id} já existe.")
            self.produtos.append(produto)
            logger.info(f"Produto {produto.nome} adicionado ao pedido com ID {produto.id}.")
        except Exception as e:
            logger.error(f"Erro ao adicionar produto {produto.nome}: {e}")

    def calcularTotal(self):
        try:
            total = sum(produto.preco for produto in self.produtos)
            if total > 100:
                desconto = total * 0.10
                total -= desconto
                logger.info(f"Desconto de 10% aplicado ao pedido de {self.cliente}. Total com desconto: R${total:.2f}.")
            else:
                logger.info(f"Total do pedido de {self.cliente}: R${total:.2f}. Sem desconto aplicado.")
            return total
        except Exception as e:
            logger.error(f"Erro ao calcular o total do pedido de {self.cliente}: {e}")
            return 0.0