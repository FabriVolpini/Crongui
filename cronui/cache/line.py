#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

f=open("/etc/cronui/cache/line15","r")
lines= f.read()
f.close() 
a=lines.split("\n")
asd=a[0]
if (asd=="#"):
    os.system("sed -i '15d' /etc/crontab")
