<<<<<<< HEAD
class Restaurant():
    """ Uma tentativa simples de modelar um cachorro. """
    def __init__(self, name, tipo):
        """ Incializa os atributos name e age """
        self.name = name
        self.tipo = tipo

    def describe_restaurant(self):
        """ Descriçao dos restautantes e estilo de cozinha. """
        print(self.name.title() + " estilo de Cozinha: " + self.tipo )

    def open_restaurant(self):
        """ Mostra se o restaurante esta aberto."""
        print("O Restaurante esta aberto")
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
>>>>>>> 08dea34b4d5a24486ed2c6b805cc670c57b31c9b
