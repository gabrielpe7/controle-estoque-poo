class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def valor_total(self):
        return self.preco * self.quantidade
    
    def registrar_entrada(self, quantidade):
        self.quantidade += quantidade
        
    def registrar_saida(self, quantidade):
        if quantidade > self.quantidade:
            return False
        
        self.quantidade -= quantidade
        return True