## Processador dos grafo ##

from os import makedirs
import math
from functools import reduce
from eficiencia import eficiência

import networkx as nx
import matplotlib.pyplot as plt
import powerlaw
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

def extrai1 (tup):
    """Extrator do índice 1 de uma tupla, útil pras funções do nx que retornam
    dicionários com os resultados"""
    return tup[1]


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
                print (' ', *args)
            else:
                arq.write (' '.join (map (str, args)))
                arq.write ('\n')

        # lê a rede do arquivo de entrada
        G = nx.read_weighted_edgelist (nomeEntrada, nodetype = int, comments = '%')
        # e acha o maior componente
        maiorComponente = max (nx.connected_component_subgraphs (G), key = len)

        distribuiçãoDeGraus = list (map (extrai1, G.degree ()))
        histograma = nx.degree_histogram (G)
        n_nós = len (G)
        probabilidadeGraus = list (map (lambda x: x / n_nós, histograma))

        # Centralidades; TODO: descobrir se rola o 'G' ou o 'maiorComponente' nessas medidas
        betweenness = np.array (nx.betweenness_centrality (G).values ())
        eigenvector = np.array (nx.eigenvector_centrality_numpy (G).values ())
        closeness = np.array (nx.closeness_centrality (G).values ())

        # Assortatividade
        assortatividade = nx.degree_assortativity_coefficient (G)

        printa ("Assortatividade:", assortatividade)

    ##  Plots  ##
    # plot da distribuição do grau
    # plt.figure ('Distribuição do grau')
    # plt.clf ()
    # plt.plot (probabilidadeGraus, 'r-', label = 'Probabilidade')
    # plt.plot (grausAcumulados, 'b-', label = 'Prob. acumulada complementar')
    # plt.title ('Distribuição do grau')
    # plt.yscale ('log')
    # plt.xscale ('log')
    # plt.legend (loc = 'lower left')
    # plt.savefig (pastaSaída + '/dist-grau.png')
    # # plot do k(i) vs cc(i)
    # plt.figure ('k(i) X cc(i)')
    # plt.clf ()
    # plt.plot (distribuiçãoDeGraus, distribuiçãoAglomeração, 'bo')
    # plt.title ('Distribuição de grau X coeficiente de aglomeração')
    # plt.xlabel ('k(i)')
    # plt.ylabel ('cc(i)')
    # plt.yscale ('log')
    # plt.xscale ('log')
    # plt.savefig (pastaSaída + '/kXcc.png')
    # # plot do coeficiente de aglomeração acumulado
    # plt.figure ('Coeficiente de aglomeração')
    # plt.clf ()
    # plt.hist (distribuiçãoAglomeração, bins = 100, histtype = 'step', normed = True, cumulative = True)
    # plt.xlabel ('cc')
    # plt.ylabel ('P (X < x)')
    # plt.title ('Distribuição de probabilidade acumulada do coeficiente de aglomeração local')
    # plt.savefig (pastaSaída + '/aglomeração.png')
