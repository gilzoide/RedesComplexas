# Exercício 1: Simular SI, SIR e SIS nos modelos BA e ER, usando transmissão reativa

from constantes import *
import epidemia
import matplotlib.pyplot as plt

def ex1 (BA, ER):
    for modelo in ['sir']:
        nome = 'BA-reativo-' + modelo
        print ('ex1 - Processando: ' + nome)
        inf, sus, rec, fim = epidemia.reativo (BA, modelo, num_iter_reativo, beta_reativo, mi_reativo)
        # plot da proporção de infectados no reativo
        plt.figure (nome)
        plt.clf ()
        plt.plot (inf[:fim], 'b-', label="Infectados")
        plt.plot (sus[:fim], 'r-', label="Suscetíveis")
        plt.plot (rec[:fim], 'g-', label="Recuperados")
        plt.legend ()
        plt.title ('Simulação reativa de epidemia na rede BA usando modelo ' + modelo)
        plt.xlabel ('t')
        plt.ylabel ('Quantidade')
        plt.savefig ('figuras/{}.png'.format (nome))

        if modelo == 'sir':
            global BA_reativo_sir
            BA_reativo_sir = inf

        nome = 'ER-reativo-' + modelo
        print ('ex1 - Processando: ' + nome)
        inf, sus, rec, fim = epidemia.reativo (ER, modelo, num_iter_reativo, beta_reativo, mi_reativo)
        # plot da proporção de infectados no reativo
        plt.figure (nome)
        plt.clf ()
        plt.plot (inf[:fim], 'b-', label="Infectados")
        plt.plot (sus[:fim], 'r-', label="Suscetíveis")
        plt.plot (rec[:fim], 'g-', label="Recuperados")
        plt.legend ()
        plt.title ('Simulação reativa de epidemia na rede BA usando modelo ' + modelo)
        plt.xlabel ('t')
        plt.ylabel ('Quantidade')
        plt.savefig ('figuras/{}.png'.format (nome))

        if modelo == 'sir':
            global ER_reativo_sir
            ER_reativo_sir = inf
