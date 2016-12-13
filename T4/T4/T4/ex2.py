# Exercício 2: Epidemia SIR reativo nas redes ER, BA, WS (p = 0.001), WS (p = 0.1)
# e BA não-linear (alpha = 0.5)

from constantes import *
import epidemia
import matplotlib.pyplot as plt
import networkx as nx

def ex2 (BA, ER):
    WS1 = nx.watts_strogatz_graph (N_redes, K_medio, 0.001)
    WS2 = nx.watts_strogatz_graph (N_redes, K_medio, 0.1)

    plt.figure ('ex2')
    plt.clf ()
    for nome in ['BA', 'ER', 'WS1 (p = 0,001)', 'WS2 (p = 0,1)']:
        G = locals ()[nome[:3]]
        print ('ex2 - Processando: ' + nome)
        inf, _, _, fim = epidemia.reativo (G, 'sir', 1000, beta_reativo, mi_reativo)
        plt.plot (inf[:fim], label = nome)

    plt.legend ()
    plt.title ('Influência da topologia da rede na simulação de epidemias')
    plt.xlabel ('t')
    plt.ylabel ('Infectados')
    plt.savefig ('figuras/ex2.png')
