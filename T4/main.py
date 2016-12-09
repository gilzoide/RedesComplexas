#!/usr/bin/env python
#!-*- conding: utf8 -*-

##  Projeto 4: as epidemia lá  ##

from processador import processa
import argparse

def main ():
    """Roda os trem"""
    parser = argparse.ArgumentParser ()
    parser.add_argument ('exs_a_rodar', nargs = argparse.REMAINDER, type = int,
            help = "Exercícios a rodar. Padrão: 1-6.")

    opts = parser.parse_args ()
    processa (opts.exs_a_rodar or [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    main ()
