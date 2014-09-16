#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

a =raw_input("¿Deseas instalar o actualizar Qt4 (esencial para este programa)?(s/n)\n")
if (a=="s"):
    os.system("sudo bash ./ins/inssupqt4.sh")

b=raw_input("¿Desea continuar la instalacion de Crontabui?(s/n)\n")
if (b=="s"):
    os.system("sudo bash ./ins/insscrontabui.sh")
    
c=raw_input("¿Desea tener un acceso directo en su escritorio(todos los usuarios)?(s/n)\n")
if (c=="s"):
    os.system("sudo bash ./ins/inssicons.sh")
