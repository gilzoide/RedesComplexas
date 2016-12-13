# Simulação de propagação de epidemias

from random import choice, random, seed

seed ()

def contato (G, modelo, iterações, A, B = 0, imunizados = None):
    imunizadosA= imunizados or set ()
    resultado_infectados = [0] * iterações
    resultado_suscetiveis = [0] * iterações
    resultado_recuperados = [0] * iterações
    fim = 0
    for nóInicial in G:
        infectados = {nóInicial}
        imunizadosA= imunizados or set ()
        try:
            for it in range (iterações):
                i = choice (tuple (infectados))
                j = choice (list (filter (lambda x: not x in imunizadosA, G[i])))
                # recuperação do passo anterior (pra poder infectar denovo)
                if modelo == 'sis' and j in infectados and random () < B:
                    infectados.remove (j)
                # tenta infectar
                if random () < A:
                    infectados.add (j)
                # recuperação
                if random () < B:
                    if modelo != 'si':
                        infectados.remove (i)
                    if modelo == 'sir':
                        imunizadosA.add (i)
                resultado_infectados[it] += len (infectados) / float(len (G))
                resultado_recuperados[it] += len (imunizadosA) / float(len (G))
                resultado_suscetiveis[it] += 1.0 - (len (infectados) / float(len (G)) + len (imunizadosA) / float(len (G)))
        # acabaram os infectados, para de rodar =]
        except Exception as ex:
            if str (ex) != "Cannot choose from an empty sequence":
                print (ex)
            if it > fim:
                fim = it
    return [x / len (G) for x in resultado_infectados], [x / len (G) for x in resultado_suscetiveis], [x / len (G) for x in resultado_recuperados], fim

def reativo (G, modelo, iterações, A, B = 0, imunizados = None):
    imunizadosA= imunizados or set ()
    resultado_infectados = [0] * iterações
    resultado_suscetiveis = [0] * iterações
    resultado_recuperados = [0] * iterações
    fim = 0
    it = 0
    for nóInicial in G:
        infectados = {nóInicial}
        imunizadosA= imunizados or set ()
        try:
            for it in range (iterações):
                i = choice (tuple (infectados))
                for j in filter (lambda x: not x in imunizadosA, G[i]):
                    # recuperação do passo anterior (pra poder infectar denovo)
                    if modelo == 'sis' and j in infectados and random () < B:
                        infectados.remove (j)
                    # tenta infectar
                    if random () < A:
                        infectados.add (j)
                # recuperação
                if random () < B:
                    if modelo != 'si':
                        infectados.remove (i)
                    if modelo == 'sir':
                        imunizadosA.add (i)
                resultado_infectados[it] += len (infectados) / float(len (G))
                resultado_recuperados[it] += len (imunizadosA) / float(len (G))
                resultado_suscetiveis[it] += 1.0 - (len (infectados) / float(len (G)) + len (imunizadosA) / float(len (G)))
        # acabaram os infectados, para de rodar =]
        except Exception as ex:
            if str (ex) != "Cannot choose from an empty sequence":
                print (ex)
            if it > fim:
                fim = it
    return [x / len (G) for x in resultado_infectados], [x / float(len (G)) for x in resultado_suscetiveis], [x / len (G) for x in resultado_recuperados], fim
