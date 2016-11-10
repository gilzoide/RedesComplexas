## Caminhada aleatória ##

import networkx as nx
import random

MAX_ITER = 1000

def caminhadaleatoria (G):
    # usa como seed o tempo do SO, pra termos resultados diferentes
    random.seed ()

    resultado = [0] * len (G)

    for nóInicial in G:
        atual = nóInicial
        for i in range (MAX_ITER):
            vizinhos = list (G[atual])
            atual = random.choice (vizinhos)
            resultado[atual - 1] += 1
    return resultado
