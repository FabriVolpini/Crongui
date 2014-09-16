#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

f=open("/etc/cronui/cache/usrs","r")
lines= f.read()
f.close() 
a=lines.split("\n")
last=a.index("")
del a[last]
for z in a:
    a="/home/"+str(z)+"/Escritorio"
    os.system("cp ./cronui/icon/Cronui "+str(a))
