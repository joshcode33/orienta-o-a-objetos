from SistemaBancario import ContaCorrente, CartaoCredito #importar a classe ContaCorrente e CartaoCredito do arquivo SistemaBancario
#isso sempre servirá para programar o sitema separadamente.

#programa
conta_Josias = ContaCorrente(nome = 'Josias', cpf = '123.456.789.00', saldo = 0, conta = '1234-5', limite = None, agencia = '0001', cartoes = [])


cartao_Josias = CartaoCredito(titular = 'Josias', conta_corrente = 'conta_Josias',)


cartao_Josias.senha = '1234'
print(cartao_Josias.senha)




