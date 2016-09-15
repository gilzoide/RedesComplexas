#!/usr/bin/env python

##  Projeto 1: Caracterização de redes complexas: Grau, clustering e caminho  ##

from glob import glob
from processador import processa

def main ():
    redes = glob ('in/*')
    for arq in redes:
        print ('Processando "%s"' % (arq))
        processa (arq)

if __name__ == '__main__':
    main ()
