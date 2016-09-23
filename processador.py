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


def processa (nomeEntrada):
    """Processa arquivo da rede, pondo as saídas na pasta com o nome 'out/<rede>'
    Saídas:
        - ?
    """
    pastaSaída = criaPastaSaída (nomeEntrada)
    with open (pastaSaída + '/stats.txt', 'w') as arq:
        def printa (*args):
            """Escreve a saída no arquivo de estatísticas, pliz"""
            arq.write (' '.join (map (str, args)))
            arq.write ('\n')
        # lê a rede do arquivo de entrada
        G = nx.read_weighted_edgelist (nomeEntrada, nodetype = int, comments = '%')
        # e acha o maior componente
        maiorComponente = max (nx.connected_component_subgraphs (G), key = len)

        distribuiçãoDeGraus = list (map (lambda t: t[1], G.degree ()))
        histograma = nx.degree_histogram (G)
        n_nós = len (G)
        probabilidadeGraus = list (map (lambda x: x / n_nós, histograma))
        grausAcumulados = np.flipud (np.cumsum (np.flipud (probabilidadeGraus)))

        # distribuição lei de potência
        leiPotência = powerlaw.Fit (distribuiçãoDeGraus, fit_method = 'KS')
        printa ('Lei de potência - Alpha:', leiPotência.power_law.alpha, '\txmin:', leiPotência.power_law.xmin)

        # cálculo de medidas globais
        printa ('Grau médio:', sum (distribuiçãoDeGraus) / n_nós)
        printa ('Segundo momento da distribuição do grau:', reduce (lambda acc, ki: acc + ki ** 2, distribuiçãoDeGraus, 0) / n_nós)
        printa ('Entropia de Shannon:', - reduce (lambda acc, prob: acc + prob * math.log (prob), grausAcumulados))
        printa ('Média do coeficiente de aglomeração local:', nx.average_clustering (G))
        printa ('Coeficiente de aglomeração pela fórmula da transitividade:', nx.transitivity (G))
        # printa ('Média dos menores caminhos:', nx.average_shortest_path_length (maiorComponente))
        printa ('Eficiência:', eficiência (G))
        printa ('Diâmetro:', nx.diameter (maiorComponente))

        # cálculo de clustering
        distribuiçãoAglomeração = list (nx.clustering (G).values ())
        printa ('Correlação de Pearson de k(i) X cc(i):', stats.pearsonr (distribuiçãoDeGraus, distribuiçãoAglomeração)[0])

    ##  Plots  ##
    # plot da distribuição do grau
    plt.figure ('Distribuição do grau')
    plt.clf ()
    plt.plot (probabilidadeGraus, 'r-', label = 'Probabilidade')
    plt.plot (grausAcumulados, 'b-', label = 'Prob. acumulada complementar')
    plt.title ('Distribuição do grau')
    plt.yscale ('log')
    plt.xscale ('log')
    plt.legend (loc = 'lower left')
    plt.savefig (pastaSaída + '/dist-grau.png')
    # plot do k(i) vs cc(i)
    plt.figure ('k(i) X cc(i)')
    plt.clf ()
    plt.plot (distribuiçãoDeGraus, distribuiçãoAglomeração, 'bo')
    plt.title ('Distribuição de grau X coeficiente de aglomeração')
    plt.xlabel ('k(i)')
    plt.ylabel ('cc(i)')
    plt.savefig (pastaSaída + '/k x cc.png')
    # plot do coeficiente de aglomeração acumulado
    plt.figure ('Coeficiente de aglomeração')
    plt.clf ()
    plt.hist (distribuiçãoAglomeração, bins = 100, histtype = 'step', normed = True, cumulative = True)
    plt.xlabel ('cc')
    plt.ylabel ('P (X < x)')
    plt.title ('Distribuição de probabilidade acumulada do coeficiente de aglomeração local')
    plt.savefig (pastaSaída + '/aglomeração.png')
