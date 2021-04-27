#!/usr/bin/env python
# -*- coding: utf8 -*-
import glob
import os
import subprocess
import socket
import sys
import time
from threading import Thread

class VirtualBoxConvert ():
    machines = []
    vbox = []
    DESTINO = "/tmp/Converted/"


    def procuraVdi(self):
        os.system("mkdir " + str(self.DESTINO))
        os.system("find /home -iname *.vdi  > /tmp/caminho ")
        os.system('find /home -iname *.vdi | cut -f 6 -d "/" > /tmp/nome')

        for file in glob.glob('/tmp/caminho'):
            for caminho in open(file, 'r'):
                if not caminho.strip().startswith('#'):
                    for i in caminho.split('\n'):
                        self.machines.append(i)

        for file in glob.glob('/tmp/nome'):
            for nome in open(file, 'r'):
                if not nome.strip().startswith('#'):
                    for j in nome.split('\n'):
                        self.vbox.append(str(j).replace('vdi','qcow2'))


    def convertVdi(self,caminho,name):
        print("Começando a conversão da imagem " + str(caminho) + "....")
        os.system("qemu-img convert -f vdi -O qcow2" + " " + str(caminho) + " " + str(self.DESTINO + name))
        print("Conversão finalizada da imagem " + name + " finalizada...." )

    def disparaThread(self):

         for i in dict(zip(self.machines, self.vbox)):


           dispara = Thread(target=self.convertVdi,args=["'" + i + "'",dict(zip(self.machines, self.vbox))[i]])
           dispara.start()




    def limpatudo(self):
        os.system("rm -rf /tmp/caminho ")
        os.system("rm -rf /tmp/nome ")


if __name__ == '__main__':

    inicia =  VirtualBoxConvert()
    inicia.procuraVdi()
    inicia.disparaThread()
    inicia.limpatudo()
