#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')

arquivos = 'cats.txt'

with open(arquivos) as files_object:
    lines = files_object.readlines()

print("Nome dos gatos: ")
for line in lines:
    print(line.strip())