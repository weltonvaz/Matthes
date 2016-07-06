#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')

def gatos(arquivos):
    with open(arquivos) as files_object:
        lines = files_object.readlines()
    print("Nome dos gatos: ")
    for line in lines:
        print(line.strip())
    
def cachorros(arquivos):
    lendoarq(arquivos)
    print("Nome dos cachorros: ")
    for line in lines:
        return line.strip()

print(gatos('cats.txt'))