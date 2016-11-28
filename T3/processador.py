#!-*- conding: utf8 -*-
# Processador dos grafo ##

from os import makedirs
import math
from functools import reduce

import networkx as nx
import igraph as ig
from igraph.drawing.colors import RainbowPalette
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


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
        print ('Bet ok')
        fastGreedy = g1.community_fastgreedy()
        print ('Fast ok')
        walktrap = g1.community_walktrap()
        print ('walk ok')
        eigen = g1.community_leading_eigenvector()
        print ('Eigen ok')

        printa ("Betweenness: ", g1.modularity(bet.as_clustering().membership))
        printa ("Fast Greedy: ", g1.modularity(fastGreedy.as_clustering().membership))
        printa ("Walktrap: ", g1.modularity(walktrap.as_clustering().membership))
        printa ("Eigenvector: ", g1.modularity(eigen))
        

def umaRede():
    color_list = ['red', 'blue', 'green', 'cyan', 'pink', 'orange', 'grey', 'yellow', 'white', 'black', 'purple']
    G = ig.Graph.Famous("Zachary")

    bet = G.community_edge_betweenness()
    fastGreedy = G.community_fastgreedy()
    walktrap = G.community_walktrap()
    eigen = G.community_leading_eigenvector()

    layout = G.layout_kamada_kawai()
    ig.plot(G, "graphbet.png", layout=layout, vertex_color=[color_list[x] for x in bet.as_clustering().membership])

    ig.plot(G, "graphfastgreedy.png", layout=layout, vertex_color=[color_list[x] for x in fastGreedy.as_clustering().membership])
    
    ig.plot(G, "graphwalk.png", layout=layout, vertex_color=[color_list[x] for x in walktrap.as_clustering().membership])
    
    color = [x for x in range(34)]
    count = 0
    for x in eigen:
        for y in x:
            color[y] = color_list[count]
        count += 1

    ig.plot(G, "grapheigen.png", layout=layout, vertex_color=color)

def le(nome):
    G = nx.read_weighted_edgelist (nome, nodetype = int, comments = '%')
    maiorComponente = max (nx.connected_component_subgraphs (G), key = len)

    adicionar = []
    for i in nx.to_edgelist(maiorComponente):
        adicionar.append(tuple([i[0], i[1], i[2]]))

    return ig.Graph().TupleList(adicionar)

def redeCriada():
    g1 = le("network.dat")

    bet = g1.community_edge_betweenness()
    fastGreedy = g1.community_fastgreedy()
    walktrap = g1.community_walktrap()
    eigen = g1.community_leading_eigenvector()

    print ("Betweenness: ", g1.modularity(bet.as_clustering().membership))
    print ("Fast Greedy: ", g1.modularity(fastGreedy.as_clustering().membership))
    print ("Walktrap: ", g1.modularity(walktrap.as_clustering().membership))
    print ("Eigenvector: ", g1.modularity(eigen))

def redeCriadaBonita(pasta):
    G = le(pasta + "/network.dat")

    bet = G.community_edge_betweenness()
    fastGreedy = G.community_fastgreedy()
    walktrap = G.community_walktrap()
    eigen = G.community_leading_eigenvector()

    layout = G.layout_kamada_kawai()

    pal = RainbowPalette(max(bet.as_clustering().membership)+1)

    ig.plot(G, pasta + "/graphbet.png", layout=layout, vertex_color=[pal[x] for x in bet.as_clustering().membership])

    pal = RainbowPalette(max(fastGreedy.as_clustering().membership)+1)

    ig.plot(G, pasta + "/graphfastgreedy.png", layout=layout, vertex_color=[pal[x] for x in fastGreedy.as_clustering().membership])
    
    pal = RainbowPalette(max(walktrap.as_clustering().membership)+1)

    ig.plot(G, pasta + "/graphwalk.png", layout=layout, vertex_color=[pal[x] for x in walktrap.as_clustering().membership])
    
    pal = RainbowPalette(len(eigen))
    color = [x for x in range(G.vcount())]
    count = 0
    for x in eigen:
        for y in x:
            color[y] = pal[count]
        count += 1

    ig.plot(G, pasta + "/grapheigen.png", layout=layout, vertex_color=color)
