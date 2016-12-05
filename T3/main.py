#!/usr/bin/env python
#!-*- conding: utf8 -*-

##  Projeto 3: Processos dinâmicos em redes complexas  ##

from glob import glob
import sys
from processador import *


def main ():
    """Roda os trem. Chame com qualquer argumento pra saída ir pro stdout e não
    pros arquivos"""
    # toStdOut = len (sys.argv) > 1
    # redes = glob ('in/*')
    # for arq in redes:
    #     print ('Processando "%s"' % (arq))
    #     processa (arq, toStdOut)
    # umaRede()
    # redeCriada()
    for i in range (0, 6):
        redeCriadaBonita('weighted_directed_nets/rede' + str (i))

if __name__ == '__main__':
    main ()
