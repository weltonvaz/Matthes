#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')

class User():
    """ Simulando usuarios. """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def descritive_user(self):
        long_name = self.first_name + ' ' + self.last_name
        return long_name.title()

    def greet_user(self):
        return 'Benvindo, ' + self.first_name.lower()

usuario1 = User('Welton', 'Vaz')
print(usuario1.descritive_user())
print(usuario1.greet_user())
