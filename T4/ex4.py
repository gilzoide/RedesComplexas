# Exercício 4: Coeficiente crítico teórico vs prático

from constantes import *
import epidemia
import matplotlib.pyplot as plt
import numpy as np

def calcula_momento (G, n):
    momento = 0
    for _, grau in G.degree ():
        momento += grau ** n
    return momento / len (G)

def ex4 (BA, ER):
    BA_lambda_crítico = K_medio / calcula_momento (BA, 2)
    print ('BA - lambda_crítico = ', BA_lambda_crítico)

    ER_lambda_crítico = K_medio / calcula_momento (ER, 2)
    print ('ER - lambda_crítico = ', ER_lambda_crítico)

    print ('ex4 - Processando reativo')
    BA_reativo = []
    ER_reativo = []
    lambdas_x = np.arange (0, 0.2, 0.01)
    for lbda in lambdas_x:
        beta = lbda / mi_reativo
        inf, _, _ = epidemia.reativo (BA, 'sis', num_iter_reativo, beta, mi_reativo)
        BA_reativo.append (inf[-1])

        inf, _, _ = epidemia.reativo (ER, 'sis', num_iter_reativo, beta, mi_reativo)
        ER_reativo.append (inf[-1])

    print ('ex4 - Processando contato')
    BA_contato = []
    ER_contato = []
    for lbda in lambdas_x:
        beta = lbda / mi_contato
        inf, _, _ = epidemia.contato (ER, 'sis', num_iter_contato, beta, mi_contato)
        ER_contato.append (inf[-1])

        inf, _, _ = epidemia.contato (BA, 'sis', num_iter_contato, beta, mi_contato)
        BA_contato.append (inf[-1])

    ## Plots
    # contato
    plt.figure ('ex4 - contato')
    plt.clf ()
    plt.title ('Coeficiente para propagação de epidemias por contato, teórico vs real')
    plt.plot (lambdas_x, BA_contato, 'b-', label = r'BA: $\lambda_c$ = {}'.format (BA_lambda_crítico))
    plt.plot (lambdas_x, ER_contato, 'r-', label = r'ER: $\lambda_c$ = {}'.format (ER_lambda_crítico))
    plt.legend ()
    plt.xlabel (r'$\lambda$')
    plt.ylabel ('Infectados')
    plt.savefig ('figuras/ex4-contato.png')
    # reativo
    plt.figure ('ex4 - reativo')
    plt.clf ()
    plt.title ('Coeficiente para propagação de epidemias reativo, teórico vs real')
    plt.plot (lambdas_x, BA_reativo, 'b-', label = r'BA: $\lambda_c$ = {}'.format (BA_lambda_crítico))
    plt.plot (lambdas_x, ER_reativo, 'r-', label = r'ER: $\lambda_c$ = {}'.format (ER_lambda_crítico))
    plt.legend ()
    plt.xlabel (r'$\lambda$')
    plt.ylabel ('Infectados')
    plt.savefig ('figuras/ex4-reativo.png')
