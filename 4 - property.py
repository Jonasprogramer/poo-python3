class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco #valor
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #getter
    @property
    def preco(self):
        return self._preco
    
    #setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor



p1 = Produto('Camisa', 'R$50')
p1.desconto(10)
print(p1.preco)