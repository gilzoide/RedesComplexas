# Processador das coisa, pra desafogar a main

import networkx as nx

from ex1 import ex1

def processa (exs_a_rodar):
    BA = nx.barabasi_albert_graph (1000, 8)
    ER = nx.erdos_renyi_graph (1000, 8 / 1000)

    if 1 in exs_a_rodar:
        ex1 (BA, ER)
