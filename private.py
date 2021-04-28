class livro:
  def __init__(self):
    self.__pages = None
  def set_pages(self, qto):
    self.__pages = qto
  def get_pages(self):
    return self.__pages
  def __contar_pagina(self):
    print('estou sendo ultilizdo')
    
#escopo global
obj_livro = livro()

'''
#visibilidade public - tenho acesso para modificar e exibir
obj_livro.pages = 120
print(obj_livro.pages)
'''
'''
atributos em python não ficam realmente privados como em outras liguagens de programação
__ - mesmo usando isso para proteger, os arquivos podemos alterá-los.
'''
#visibilidade privado - não terá acesso nem exibição ou modificação
obj_livro.__pages = 120
print(obj_livro.__pages)
obj_livro.set_pages(150)
print(obj_livro.get_pages())
#obj_livro.__contar_pagina()