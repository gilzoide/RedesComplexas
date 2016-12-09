# Exercício 3: Simular SI, SIR e SIS nos modelos BA e ER, usando transmissão por contato
# (pra comparar com o reativo)

from constantes import *
import epidemia
import matplotlib.pyplot as plt

def _processando (nome):
    print ('ex3 - Processando: ' + nome)

def ex3 (BA, ER):
    modelo = 'sir'

    # evita ressimular o reativo, se já tiver rodado o ex1
    global BA_reativo_sir
    global ER_reativo_sir
    if 'BA_reativo_sir' not in globals ():
        _processando ('BA-reativo-sir')
        BA_reativo_sir, _, _ = epidemia.reativo (BA, modelo, num_iter_reativo, beta_reativo, mi_reativo)
        _processando ('ER-reativo-sir')
        ER_reativo_sir, _, _ = epidemia.reativo (ER, modelo, num_iter_reativo, beta_reativo, mi_reativo)


    nome = 'BA-contato-' + modelo
    _processando (nome)
    inf, _, _ = epidemia.contato (BA, modelo, num_iter_contato, beta_contato, mi_contato)
    # plot da proporção de infectados no contato
    plt.figure (nome)
    plt.clf ()
    plt.plot (inf, 'b-', BA_reativo_sir, 'r-')
    plt.title ('Contato vs reativo na rede BA usando modelo ' + modelo)
    plt.xlabel ('t')
    plt.ylabel ('Infectados')
    plt.savefig ('figuras/BA-reativoXcontato.png')

    nome = 'ER-contato-' + modelo
    _processando (nome)
    inf, _, _ = epidemia.contato (ER, modelo, num_iter_contato, beta_contato, mi_contato)
    # plot da proporção de infectados no contato
    plt.figure (nome)
    plt.clf ()
    plt.plot (inf, 'b-', ER_reativo_sir, 'r-')
    plt.title ('Contato vs reativo na rede ER usando modelo ' + modelo)
    plt.xlabel ('t')
    plt.ylabel ('Infectados')
    plt.savefig ('figuras/ER-reativoXcontato.png')


