class ContaCorrente():

    def __init__(self, saldo, nome, cpf, conta, limite):
        self.saldo = 0
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
        self.limite = None 
    def mostrar_saldo(self):
        print('Seu saldo atual é de U${:.2f}'.format(self.saldo))


    def depositar(self, valor):
        self.saldo += valor

    def limite_conta(self):
        self.limite = -100
        return self.limite 
    
    def sacar(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Saldo insuficiente')
            self.mostrar_saldo()
        else:    
             self.saldo -= valor

    def consultar_limite_cheque(self):
        print("Seu limite de Cheque é de U${}".format(self.limite))
    
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        conta_destino.saldo += valor
#programa
conta_Josias = ContaCorrente(nome = 'Josias', cpf = '123.456.789.00', saldo = 0, conta = '1234-5', limite = None)#sempre adicionar todas os métodos do da classe.
conta_Josias.mostrar_saldo()

#resultado
conta_Josias.depositar(8765)
conta_Josias.mostrar_saldo()

conta_Josias.sacar(10000)
conta_Josias.mostrar_saldo()

print(conta_Josias.nome)
print(conta_Josias.cpf)   



  