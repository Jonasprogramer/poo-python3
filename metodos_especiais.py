class conta:
    #construct
    def __init__(self, conta):
        self.Nconta = conta
        self.__saldo = None
        self.__tipo = None

    #setters alterar atributos
    def setter_saldo(self, saldo):
        self.__saldo = saldo
    def setter_tipo(self, tipo):
        self.__tipo = tipo
    
    #getters acessar atributos
    def getter_saldo(self):
        return self.__saldo
    def getter_tipo(self):
        return self.__tipo


#escopo global
client = conta('1087-1')
client.setter_saldo(100)
print('seu saldo é de {} reais'.format(client.getter_saldo()))


