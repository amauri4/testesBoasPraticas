# Classe básica de produto
class Produto:
    def __init__(self, id:int, nome:str, preco:float):
        self.id = id
        self.nome = nome
        self.preco = preco