from random import randint
class Pessoa:
    ano_atual = 2021
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self): #metodo de objeto - instância
        print(self.ano_atual - self.idade)
    
    @classmethod #não precisa ter atributos disponíveis em outras instancias, refere-se a class
    def por_ano_nacimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade) #manda direto para a propria classe, fabrica o objeto
    
    @staticmethod #funciona como uma função normal só que colocada dentro da class, não se pode usar self nem cls.
    def gerar_id():
        rand = randint(10000, 19999)
        return rand
        


p1 = Pessoa.por_ano_nacimento('Jonas', 1999)
p1.get_ano_nascimento()

print(Pessoa.gerar_id())
print(p1.gerar_id())