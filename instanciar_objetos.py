#criando uma classe
class caneta:
    x = 'preta'
print(caneta)

#criando um objeto
obj = caneta()
print(obj.x) #sem o atributo mostra apenas o local da memória onde o objeto está instanciado

#---------------------------------------------------------------------------------------------------------------------

#funcao __init__() - Todas as classes possuem uma função chamada __init __ (), que sempre é executada quando a classe está sendo iniciada. usada para atribuir valores às propriedades do objeto ou outras operações que são necessárias quando o objeto está sendo criado:

class bic_modelo:
    def __init__(self, cor, tinta): 
        #O self parâmetro é uma referência à instância atual da classe e é usado para acessar variáveis ​​que pertencem à classe. 
        #Ele não precisa ser nomeado self, você pode chamá-lo do que quiser, mas deve ser o primeiro parâmetro de qualquer função na classe.
    #atributos
        self.cor = cor
        self.tinta = tinta
    #métodos    
    def escrever(self):
        print('Caneta bic {} com {}% de tinta'.format(self.cor, self.tinta))

objeto = bic_modelo('preta', 90)
objeto.escrever()

#modificar atributo/propriedade
objeto.cor = 'Azul'
objeto.escrever()

#excluir atributo/obj
'''
del objeto.cor
del objeto
'''
#declaração de passagem serve para evitar erros
class vazia:
    pass