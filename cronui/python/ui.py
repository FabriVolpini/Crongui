#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.uic import *
import ConfigParser
import os

class Inicio(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("/etc/cronui/python/botones.ui",self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    def nueva(self):
        ventana=Main().show()
        self.close()

class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("/etc/cronui/python/crontabui.ui",self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.limpiar()
    
    def crear(self):
        self.file="actualcron.txt"
        f=self.file
        a=str(self.ui.lineacron.text())
        s=open(self.file,"w")      
        s.write(str(a)+"\n")
        s.close()
        os.system("xterm -e sudo bash /etc/cronui/bash/perms.sh")
        self.limpiar()

    
    def texto(self):
        minuto=self.minuto
        hora=self.hora
        dia=self.dia
        mes=self.mes
        diasemana=self.diasemana
        usr=self.usr
        com=self.com
        if (minuto=="-1"):
            minuto = "*"
        if (dia=="-1"):
            dia = "*"
        if (hora=="-1"):
            hora = "*"
        if (mes=="0"):
            mes= "*"
        if (diasemana=="0"):
            diasemana= "*"
        todo=minuto+" "+hora+"    "+dia+" "+mes+" "+diasemana+"    "+usr+"    "+com
        self.ui.lineacron.setText(todo)
        self.todo=todo
        
    def minutos(self):
        minute=self.ui.minbarra.value()
        self.minuto=str(minute)
        self.texto()

    def horas(self):
        hour=self.ui.horabarra.value()
        self.hora=str(hour)
        self.texto()

    def dias(self):
        day=self.ui.diabarra.value()
        self.dia=str(day)
        self.texto()

    def meses(self):
        month=self.ui.mesbox.currentIndex()
        self.mes=str(month)
        self.texto()

    def diassemana(self):
        dayweek=self.ui.diasbox.currentIndex()
        self.diasemana=str(dayweek)
        self.texto()
        
    def usuario(self):
        uss=self.ui.userline.text()
        self.usr=str(uss)
        self.texto()
        
    def comando(self):
        self.com=self.ui.comline.text()
        self.texto()

    def limpiar(self):
        self.ui.lineacron.setText("* *    * * *    root    ")
        self.ui.userline.setText("root")
        self.ui.comline.setText("")
        self.ui.diabarra.setValue(-1)
        self.ui.horabarra.setValue(-1)
        self.ui.minbarra.setValue(-1)
        self.ui.diasbox.setCurrentIndex(0)
        self.ui.mesbox.setCurrentIndex(0)
        self.minuto="-1"
        self.hora="-1"
        self.dia="-1"
        self.mes="0"
        self.diasemana="0"
        self.usr="root"
        self.com=""

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())
