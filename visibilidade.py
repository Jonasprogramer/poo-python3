#visibilidade public, protect and private
class caneta:
   def __init__(self):
       self.cor = 'Eu sou público'
       self._tinta = 'Eu sou protegido'
       self.__tampa = 'Eu sou privado'

obj = caneta()
print(obj.cor)
print(obj._tinta)
print(obj.__tampa)