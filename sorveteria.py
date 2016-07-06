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

class IceCreamStand(Restaurant):
    """ Modela uma Sorveteria. """
    def __init__(self, nome, tipo, *flavour):
        Restaurant.__init__(self, nome, tipo)
        self.flavour = flavour

    def sabores(self):
        return 'sabores: ' + str(self.flavour)
            

meu_restaurante = IceCreamStand('Salada','Italiana','napolitano','chocolate','morango')

meu_restaurante.describe_restaurant()
print(meu_restaurante.sabores())
print(meu_restaurante.open_restaurant())
