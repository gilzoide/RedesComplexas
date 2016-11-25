#!-*- conding: utf8 -*-
# Processador dos grafo ##

from os import makedirs
import math
from functools import reduce

import networkx as nx
import igraph as ig
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from caminhadaleatoria import caminhadaleatoria

def criaPastaSaída (entrada):
    """Cria a pasta de saída (se precisar) baseado no nome da entrada, e retorna
    o nome da pasta"""
    nome = entrada.replace ('in', 'out', 1)
    # tenta criar pasta
    try:
        makedirs (nome)
    except Exception as ex:
        pass

    return nome


def processa (nomeEntrada, toStdOut = False):
    """Processa arquivo da rede, pondo as saídas na pasta com o nome 'out/<rede>'
    Saídas:
        - ?
    """
    pastaSaída = criaPastaSaída (nomeEntrada)
    with open (pastaSaída + '/stats.txt', 'w') as arq:
        def printa (*args):
            """Escreve a saída no arquivo de estatísticas, pliz"""
            if toStdOut:
                print (nomeEntrada, '\t', *args)
            else:
                arq.write (' '.join (map (str, args)))
                arq.write ('\n')

        # lê a rede do arquivo de entrada
        G = nx.read_weighted_edgelist (nomeEntrada, nodetype = int, comments = '%')
        maiorComponente = max (nx.connected_component_subgraphs (G), key = len)

        adicionar = []
        for i in list(nx.to_edgelist(maiorComponente)):
            adicionar.append(tuple([i[0], i[1]]))
        g1 = ig.Graph().TupleList(adicionar)
        print ('Start')
        bet = g1.community_edge_betweenness()
        fastGreedy = g1.community_fastgreedy()
        walktrap = g1.community_walktrap()
        eigen = g1.community_leading_eigenvector()

        printa ("Betweenness: ", g1.modularity(bet.as_clustering().membership))
        printa ("Fast Greedy: ", g1.modularity(fastGreedy.as_clustering().membership))
        printa ("Walktrap: ", g1.modularity(walktrap.as_clustering().membership))
        printa ("Eigenvector: ", g1.modularity(eigen))
        

