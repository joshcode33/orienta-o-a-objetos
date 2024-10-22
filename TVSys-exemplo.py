#Criando a nossa 1° classe em Python
#Sempre que você quiser criar uma classe, voce vai fazer:

#class name.class(object)

#Dentro da classe, você vai criar a "função" (método) __init__
#Esse método é quem define o que acontece quando você cria uma instância da Classe

#Vamos ver um exemplo para ficar mais claro, com o caso da televisão que a gente vinha comentando

#classes
class TV:#nome da classe
                        #podemos adicionar quantas funções nós quisermos em nosso programa, desde que não substitua a funçao principal self
    def __init__(self, tamanho, canal, volume):  #funções da tv(método)
        self.cor = 'preta'
        self.status = False
        self.tamanho = tamanho
        self.canal = canal
        self.volume = volume
                            #nova função para selecionar canais (novo_canal)
    def mudar_canal(self, novo_canal): #sempre deixar a função "self" em primeira função
        self.canal = novo_canal
        print("Canal alterado para {}".format(novo_canal))


#programa
tv_sala = TV( tamanho = 50, canal = "Facebook", volume = 25 ) #variável
tv_quarto = TV( tamanho = 75, canal = "Youtube", volume = 65 ) #variável



tv_sala.mudar_canal("Youtube")#modificacao canal
tv_quarto.mudar_canal("Xbox One")


print(tv_sala.canal) #resultado da função
print(tv_quarto.canal) #resultado da função
print(tv_sala.tamanho)
print(tv_quarto.tamanho)
print(tv_sala.volume)
print(tv_quarto.volume) 








