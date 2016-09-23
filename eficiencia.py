## Módulo calculador de eficiência ##

import networkx as nx

def eficiência (G):
    """Calcula eficiência da rede G"""
    E = 0
    menoresCaminhos = dict (nx.all_pairs_shortest_path_length (G))
    nós = G.nodes ()
    n_nós = len (G)
    for i in nós:
        for j in nós:
            if i != j:
                try:
                    E += 1 / menoresCaminhos[i][j]
                except:
                    pass
    return E / (n_nós * (n_nós - 1))
