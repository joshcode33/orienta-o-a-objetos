
from random import randint 

class Agencia:


    def __init__(self, telefone, cnpj, numero):
        self._cnpj = cnpj
        self.numero = numero
        self._telefone = telefone
        self.caixa = 0
        self.clientes = []
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print("Caixa Insuficiente. Caixa atual{}".format(self.caixa))
        else:
            print("Caixa OK. Caixa atual{}".format(self.caixa))

    def emprestar_dinheiro(self, cpf, juros, caixa):
        if self.caixa > 1000000:
            self.emprestimos.append((cpf, juros, caixa))

        else:
            print("Emprestimo não realizado. Dinheiro em Caixa insuficiente")

    def adiconar_cliente(self, nome, cpf, patrimonio, caixa):
        self.clientes.append((nome, cpf, patrimonio))                  


class AgenciaPremium(Agencia):

    def __init__(self, site, cnpj, telefone, numero):
        self.site = site
        super().__init__(cnpj, telefone, numero = 1000)#chama a classe pai.
        self.caixa = 10000000
        self.caixa_picpay = 0

    def depositar_picpay(self, valor):
       self.caixa -= valor
       self.caixa_picpay += valor
    
    def sacar_picpay(self, valor):
        self.caixa_picpay -= valor
        self.caixa += valor

class AgenciaComum(Agencia):

    def __init__(self, cnpj, telefone, numero):
        super().__init__(cnpj, telefone, numero = randint(1001, 9999))#chama a classe pai.
        self.caixa = 100000

    def depositar_picpay(self, valor):
       self.caixa -= valor
       self.caixa_picpay += valor
    
    def sacar_picpay(self, valor):
        self.caixa_picpay -= valor
        self.caixa += valor   



agencia1 = Agencia(cnpj= '123.456.789.00', telefone = '13991234-5678', numero = '0001')

agenciapremium = AgenciaPremium('www.agenciapremium.com', telefone = '13991234-5678', numero = '0001', cnpj = '123.456.789.00')
agenciapremium.depositar_picpay(2000)

agenciacomum = AgenciaComum(cnpj = '123.456.789.00', telefone = '13991234-5678', numero = '0001')
agenciacomum.depositar_picpay(1000)