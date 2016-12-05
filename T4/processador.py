# Processador das coisa, pra desafogar a main

import networkx as nx
import epidemia

def processa ():
    BA = nx.barabasi_albert_graph (1000, 8)
    ER = nx.erdos_renyi_graph (1000, 8 / 1000)
    
    for modelo in ['si', 'sis', 'sir']:
        inf, susc, rec = epidemia.contato (BA, modelo, 3000, 
