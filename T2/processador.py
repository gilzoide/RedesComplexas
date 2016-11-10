## Processador dos grafo ##

from os import makedirs
import math
from functools import reduce

import networkx as nx
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

        # if nomeEntrada != 'in/as-caida20071105.CAIDA':
            # caminhada = caminhadaleatoria (G)

    ##  Plots  ##
    # plot do 'k vs knn'
    plt.figure ('k X knn(k)')
    plt.clf ()
    plt.plot (distribuiçãoKnn,  'b-')
    plt.title ('Distribuição do grau')
    plt.xlabel ('k')
    plt.ylabel ('knn (k)')
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
    pirso = stats.pearsonr (eigenvector, pageRank)[0]
    plt.loglog (eigenvector, pageRank, 'bo', label = 'Pearson: ' + str (pirso))
    plt.legend (loc = 'lower right', scatterpoints = 0)
    plt.xlabel ('eigenvector (i)')
    plt.ylabel ('pagerank (i)')
    plt.title ('Eigenvector centrality X Page rank')
    plt.savefig (pastaSaída + '/eigXpagerank.png')
    # if nomeEntrada != 'in/as-caida20071105.CAIDA':
        # # plot do k vs caminhada
        # plt.figure ('k X caminhada aleatória')
        # plt.clf ()
        # pirso = stats.pearsonr (distribuiçãoDeGraus, caminhada)[0]
        # plt.plot (distribuiçãoDeGraus, caminhada,  'bo', label = 'Pearson: ' + str (pirso))
        # plt.legend (loc = 'lower right', scatterpoints = 0)
        # plt.title ('Distribuição do grau X Caminhada aleatória')
        # plt.xlabel ('k (i)')
        # plt.ylabel ('caminhada (i)')
        # plt.savefig (pastaSaída + '/kXcaminhada.png')
        # # plot do eigenvector vs caminhada
        # plt.figure ('eigenvector X caminhada aleatória')
        # plt.clf ()
        # pirso = stats.pearsonr (eigenvector, caminhada)[0]
        # plt.plot (eigenvector, caminhada,  'bo', label = 'Pearson: ' + str (pirso))
        # plt.legend (loc = 'lower right', scatterpoints = 0)
        # plt.title ('Eigenvector centrality X Caminhada aleatória')
        # plt.xlabel ('eigenvector (i)')
        # plt.ylabel ('caminhada (i)')
        # plt.savefig (pastaSaída + '/eigXcaminhada.png')
