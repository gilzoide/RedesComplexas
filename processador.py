## Processador dos grafo ##

from os import makedirs
import math
from functools import reduce

import networkx as nx
import matplotlib.pyplot as plt
import powerlaw
import numpy as np

def criaPastaSaída (entrada):
    """Cria a pasta de saída (se precisar) baseado no nome da entrada, e retorna
    o nome da pasta"""
    nome = entrada.replace ('in', 'out')
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
    def printa (*args):
        """Função pra printar com uma identaçãozinha, pra facilitar a vida =]"""
        print (' ', *args)
    # lê o arquivo de entrada
    G = nx.read_edgelist (nomeEntrada, nodetype = int, comments = '%')
    # e acha o maior componente
    G = max (nx.connected_component_subgraphs (G), key = len)

    distribuiçãoDeGraus = list (G.degree ().values ())
    histograma = nx.degree_histogram (G)
    n_nós = len (G)
    probabilidadeGraus = np.cumsum (list (map (lambda x: x / n_nós, histograma)))

    # distribuição lei de potência
    leiPotência = powerlaw.Fit (distribuiçãoDeGraus, fit_method = 'KS')
    printa ('Lei de potência - Alpha:', leiPotência.power_law.alpha, '\txmin:', leiPotência.power_law.xmin)

    # cálculo de medidas globais
    printa ('Grau médio:', sum (distribuiçãoDeGraus) / n_nós)
    printa ('Entropia de Shannon:', - reduce (lambda acc, prob: acc + prob * math.log (prob), probabilidadeGraus))
    printa ('Média do coeficiente de aglomeração:', nx.average_clustering (G))
    printa ('Coeficiente de aglomeração pela fórmula da transitividade:', nx.transitivity (G))
    printa ('Média dos menores caminhos:', nx.average_shortest_path_length (G))
    printa ('Diâmetro:', nx.diameter (G))

    # plot da distribuição do grau
    plt.subplot (211)
    plt.plot (histograma)
    plt.title (nomeEntrada)
    plt.yscale ('log')
    plt.xscale ('log')
    # plot da distribuição acumulada do grau
    plt.subplot (212)
    plt.plot (np.cumsum (histograma))
    plt.title (nomeEntrada)
    plt.yscale ('log')
    plt.xscale ('log')
    plt.show ()

    nomeRede = criaPastaSaída (nomeEntrada)
