#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('clear')

class Employee():
    """ Cria a classe empregado, Curso Intensivo de Python."""
    def __init__(self, nome, sobrenome, sal_anual):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sal_anual = sal_anual

    def give_raise(self, aumento = 5000):
        """ Aumento anual padronizado. """
        self.sal_anual = self.sal_anual + aumento

    def contracheque(self):
        print(self.nome + ' ' + self.sobrenome)
        print('Salario Anual:' , self.sal_anual)
        
