# Simulação de propagação de epidemias

from random import choice, random, seed

seed ()

def contato (G, modelo, iterações, A, B = 0, imunizados = None):
    imunizados = imunizados or set ()
    resultado_infectados = [0] * iterações
    resultado_suscetiveis = [0] * iterações
    resultado_recuperados = [0] * iterações
    for nóInicial in G:
        infectados = {nóInicial}
        try:
            for it in range (iterações):
                i = choice (tuple (infectados))
                j = choice (list (filter (lambda x: not x in imunizados, G[i])))
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
                        imunizados.add (i)
                
                resultado_infectados[it] += len (infectados) / len (G)
                resultado_recuperados[it] += len (imunizados) / len (G)
                resultado_suscetiveis[it] += 1 - (resultado_infectados[it] + resultado_recuperados[it])
        # acabaram os infectados, para de rodar =]
        except:
            pass
    return [x / len (G) for x in resultado_infectados], [x / len (G) for x in resultado_suscetiveis], [x / len (G) for x in resultado_recuperados]

def reativo (G, modelo, iterações, A, B = 0, imunizados = None):
    imunizados = imunizados or set ()
    resultado_infectados = [0] * iterações
    resultado_suscetiveis = [0] * iterações
    resultado_recuperados = [0] * iterações
    for nóInicial in G:
        infectados = {nóInicial}
        try:
            for it in range (iterações):
                i = choice (tuple (infectados))
                for j in filter (lambda x: not x in imunizados, G[i]):
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
                        imunizados.add (i)
                resultado_infectados[it] += len (infectados) / len (G)
                resultado_recuperados[it] += len (imunizados) / len (G)
                resultado_suscetiveis[it] += 1 - (resultado_infectados[it] + resultado_recuperados[it])
        # acabaram os infectados, para de rodar =]
        except:
            pass
    return [x / len (G) for x in resultado_infectados], [x / len (G) for x in resultado_suscetiveis], [x / len (G) for x in resultado_recuperados]
