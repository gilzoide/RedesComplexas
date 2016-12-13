# Exercício 5: Imunização em pontos aleatórios vs hubs

from constantes import *
import epidemia

import matplotlib.pyplot as plt
import random
import numpy as np
import math

def _tempo_acabou (lst):
    """Acha o índice do último valor não zero da lista, que é quando a epidemia acabou"""
    for i in range (len (lst) - 1, 0, -1):
        if lst[i] != 0:
            return i

def ex5 (BA):
    maiores_graus = sorted (BA, key = lambda i: BA.degree (i), reverse = True)
    resultado_rand = []
    resultado_hubs = []
    porcentagens = np.arange (0.05, 0.35, 0.05)

    print ('ex5 - Processando simulações')
    for porcentagem_imunizados in porcentagens:
        numero_imunizados = math.floor (porcentagem_imunizados * len (BA))

        # imunizando aleatórios
        rand_imunizados = set (random.sample (list (BA), numero_imunizados))
        inf, _, _, _ = epidemia.reativo (BA, 'sir', 1000, beta_reativo, mi_reativo, rand_imunizados)
        resultado_rand.append (_tempo_acabou (inf))
        # imunizando hubs
        hubs_imunizados = set (maiores_graus[:numero_imunizados])
        inf, _, _, _ = epidemia.reativo (BA, 'sir', 1000, beta_reativo, mi_reativo, hubs_imunizados)
        resultado_hubs.append (_tempo_acabou (inf))

    plt.figure ('ex5')
    plt.clf ()
    plt.title ('Imunização de nós aleatórios vs hubs na rede BA')
    plt.plot (porcentagens, resultado_rand, 'b-', label = 'Imunização aleatória')
    plt.plot (porcentagens, resultado_hubs, 'r-', label = 'Imunização de hubs')
    plt.legend ()
    plt.xlabel ('% imunizados')
    plt.ylabel ('Duração da epidemia (iterações)')
    plt.savefig ('figuras/ex5.png')
