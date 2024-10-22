from datetime import datetime
import pytz

class ContaCorrente():


    @staticmethod#metodos estáticos, não precisam de nenhum objeto para ser executado.
    def _def_data_hora():                           
             fuso_BR = pytz.timezone('Brazil/East')
             horario_BR = datetime.now(fuso_BR)
             return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    
    def __init__(self, saldo, nome, cpf, conta, limite):
        self.saldo = 0
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
        self.limite = None
        self.transacoes = []

    def mostrar_saldo(self):
        print('Seu saldo atual é de U${:.2f}'.format(self.saldo))



    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._def_data_hora()))


    def limite_conta(self):
        self.limite = -100
        return self.limite 
    
    def sacar(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Saldo insuficiente')
            self.mostrar_saldo()
        else:    
             self.saldo -= valor
             self.transacoes.append((-valor, self.saldo, ContaCorrente._def_data_hora()))

    def consultar_limite_cheque(self):
        print("Seu limite de Cheque é de U${}".format(self.limite))
    
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._def_data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._def_data_hora()))

    def consultar_transacoes_historicas(self):
        print('Historico de transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)




#programa
conta_Josias = ContaCorrente(nome = 'Josias', cpf = '123.456.789.00', saldo = 0, conta = '1234-5', limite = None)#sempre adicionar todas os métodos do da classe.
conta_Josias.mostrar_saldo()

#resultado
conta_Josias.depositar(8765)
conta_Josias.mostrar_saldo()

print(conta_Josias.nome)
print(conta_Josias.cpf)   

print('-' * 20)
conta_Josias.consultar_transacoes_historicas()

print('-' * 20)
conta_JohnLennon = ContaCorrente(nome = 'JohnLennon', cpf = '123.456.789.00', saldo = 0, conta = '1234-5', limite = None)
conta_Josias.transferir(1000, conta_JohnLennon)

conta_Josias.mostrar_saldo()
conta_JohnLennon.mostrar_saldo()

conta_Josias.consultar_transacoes_historicas()
conta_JohnLennon.consultar_transacoes_historicas()  


  