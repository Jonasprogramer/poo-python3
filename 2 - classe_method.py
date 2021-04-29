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


p1 = Pessoa.por_ano_nacimento('Jonas', 1999)
p1.get_ano_nascimento()