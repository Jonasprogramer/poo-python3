class livro:
  def __init__(self):
    self.__pages = None
  def set_pages(self, qto):
    self.__pages = qto
  def get_pages(self):
    return self.__pages
    
#escopo global
obj_livro = livro()
'''
property - linkar o getter and setter de um atributo
'''
