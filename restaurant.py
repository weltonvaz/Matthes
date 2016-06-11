import os
os.system('clear')


class Restaurant():
    """ Modela um Restaurante. """

    def __init__(self, nome, tipo):
        """ Incializa os atributos nome e tipo."""
        self.restaurant_name = nome
        self.cuisine_type = tipo

    def describe_restaurant(self):
        """ Metodo para Descrição do Restaurante """
        print("Nome do Restaurante: " + meu_restaurante.restaurant_name.title())
        print("Estilo da Cozinha: " + meu_restaurante.cuisine_type)

    def open_restaurant(self):
        """ Simula um cachorro rolandp em resposta a um comando."""
        return "Restaurante esta aberto"

meu_restaurante = Restaurant('Albatroz','Francesa')

meu_restaurante.describe_restaurant()
print(meu_restaurante.open_restaurant())
