#!/usr/bin/env python

##  Projeto 2: Centralidade e correlação do grau em redes complexas  ##

from glob import glob
import sys
from processador import processa


def main ():
    """Roda os trem. Chame com qualquer argumento pra saída ir pro stdout e não
    pros arquivos"""
    toStdOut = len (sys.argv) > 1
    redes = glob ('in/*')
    for arq in redes:
        print ('Processando "%s"' % (arq))
        processa (arq, toStdOut)

if __name__ == '__main__':
    main ()
