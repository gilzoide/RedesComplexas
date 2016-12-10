# Processador das coisa, pra desafogar a main

import networkx as nx
from constantes import *

from ex1 import ex1
from ex2 import ex2
from ex3 import ex3
from ex4 import ex4
from ex5 import ex5

def processa (exs_a_rodar):
    BA = nx.barabasi_albert_graph (N_redes, K_medio)
    ER = nx.erdos_renyi_graph (N_redes, K_medio / N_redes)

    if 1 in exs_a_rodar:
        ex1 (BA, ER)
    if 2 in exs_a_rodar:
        ex2 (BA, ER)
    if 3 in exs_a_rodar:
        ex3 (BA, ER)
    if 4 in exs_a_rodar:
        ex4 (BA, ER)
    if 5 in exs_a_rodar:
        ex5 (BA)
