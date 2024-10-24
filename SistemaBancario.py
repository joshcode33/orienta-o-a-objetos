from datetime import datetime #importar a biblioteca de horários para marcar históricos de transações
import pytz
from random import randint#importar para random dos numeros de cartões.
import secrets
import string

class ContaCorrente():

    """
    Classe que define uma conta corrente
    Atributos:
        saldo = 0
        nome = Nome do cliente
        cpf = Cpf do cliente
        conta = Conta corrente
        limite = Limite da conta
        transacoes = Lista de transações
    """


    @staticmethod#metodos estáticos, não precisam de nenhum objeto para ser executado.
    def _def_data_hora():                           
             fuso_BR = pytz.timezone('Brazil/East')
             horario_BR = datetime.now(fuso_BR)
             return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    
    def __init__(self, saldo, nome, cpf, conta, limite, agencia, cartoes):
        self._saldo = 0
        self.nome = nome #underlines servem para tornar o atributo privado.
        self.cpf = cpf
        self._agencia = agencia
        self._conta = conta
        self._limite = None
        self._transacoes = []
        self._cartoes = []

    def mostrar_saldo(self):
        print('Seu saldo atual é de U${:.2f}'.format(self._saldo))



    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._def_data_hora()))


    def limite_conta(self):
        self._limite = -100
        return self._limite 
    
    def sacar(self, valor):
        if self._saldo - valor < self.limite_conta():
            print('Saldo insuficiente')
            self.mostrar_saldo()
        else:    
             self._saldo -= valor
             self._transacoes.append((-valor, self._saldo, ContaCorrente._def_data_hora()))

    def consultar_limite_cheque(self):
        print("Seu limite de Cheque é de U${}".format(self._limite))
    
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self.saldo, ContaCorrente._def_data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino.saldo, ContaCorrente._def_data_hora()))

    def consultar_transacoes_historicas(self):
        print('Historico de transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)


class CartaoCredito:

    @staticmethod#metodos estáticos, não precisam de nenhum objeto para ser executado.
    def _def_data_hora():                           
             fuso_BR = pytz.timezone('Brazil/East')
             horario_BR = datetime.now(fuso_BR)
             return horario_BR#remover a string de data para o mês e o ano.

    def __init__(self, titular, conta_corrente):
        self.numero = randint (1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._def_data_hora().month, CartaoCredito._def_data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint (0, 9), randint (0, 9), randint (0, 9))
        self.limite = 3600
        self._senha = '5678'
        self.conta_corrente = ContaCorrente
        conta_corrente._cartoes.append(self)

        
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
          self._senha = valor
          print('Senha alterada com sucesso')
        else:
           print('Nova Senha inválida')
             



  