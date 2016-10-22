## Processador dos grafo ##

from os import makedirs
import math
from functools import reduce

import networkx as nx
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
                print (' ', *args)
            else:
                arq.write (' '.join (map (str, args)))
                arq.write ('\n')

        # lê a rede do arquivo de entrada
        G = nx.read_weighted_edgelist (nomeEntrada, nodetype = int, comments = '%')
        # e acha o maior componente
        maiorComponente = max (nx.connected_component_subgraphs (G), key = len)

        distribuiçãoDeGraus = list (map (lambda t: t[1], G.degree ()))

        # knn, assortatividade e talz
        knn = nx.k_nearest_neighbors (G)
        distribuiçãoKnn = list (knn.values ())
        ks = list (knn.keys ())
        assortatividade = nx.degree_assortativity_coefficient (G)
        printa ("Assortatividade:", assortatividade)
        printa ("Pearson:", stats.pearsonr (ks, distribuiçãoKnn)[0])
        printa ("Spearman:", stats.spearmanr (ks, distribuiçãoKnn)[0])

        # Centralidades; TODO: descobrir se rola o 'G' ou o 'maiorComponente' nessas medidas
        betweenness = list (nx.betweenness_centrality (G).values ())
        eigenvector = list (nx.eigenvector_centrality_numpy (G).values ())
        closeness = list (nx.closeness_centrality (G).values ())
        pageRank = list (nx.pagerank_numpy (G).values ())


    ##  Plots  ##
    # plot do 'k vs knn'
    plt.figure ('k X knn(k)')
    plt.clf ()
    plt.plot (distribuiçãoKnn,  'b-')
    plt.title ('Distribuição do grau')
    plt.xlabel ('k')
    plt.ylabel ('knn (k)')
    # plt.yscale ('log')
    # plt.xscale ('log')
    plt.savefig (pastaSaída + '/kXknn.png')
    # plot do k(i) vs bet(i)
    plt.figure ('k(i) X betweenness(i)')
    plt.clf ()
    pirso = stats.pearsonr (distribuiçãoDeGraus, betweenness)[0]
    plt.loglog (distribuiçãoDeGraus, betweenness, 'bo', label = 'Pearson: ' + str (pirso))
    plt.legend (loc = 'lower right', scatterpoints = 0)
    plt.title ('Distribuição de grau X Betweenness centrality')
    plt.xlabel ('k(i)')
    plt.ylabel ('bet(i)')
    plt.savefig (pastaSaída + '/kXbet.png')
    # plot do coeficiente de aglomeração acumulado
    plt.figure ('eigen X pagerank')
    plt.clf ()
    plt.plot (eigenvector, pageRank, 'bo')
    plt.xlabel ('eigenvector (i)')
    plt.ylabel ('pagerank (i)')
    plt.yscale ('log')
    plt.xscale ('log')
    plt.title ('Eigenvector centrality X Page rank')
    plt.savefig (pastaSaída + '/eigXpagerank.png')
