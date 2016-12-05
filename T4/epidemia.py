# Simulação de propagação de epidemias

from random import choice, random, seed

seed ()

def contato (G, modelo, iterações, A, B = 0, imunizados = []):
    resultado_infectados = [0] * iterações
    resultado_suscetiveis = [0] * iterações
    resultado_recuperados = [0] * iterações
    for nóInicial in G:
        infectados = [nóInicial]
        for it in range (iterações):
            i = choice (infectados)
            j = choice (filter (lambda x: not x in imunizados, G[i]))
            # recuperação do passo anterior (pra poder infectar denovo)
            if modelo == 'sis' and j in infectados and random () < B:
                infectados.remove (j)
            # tenta infectar
            if random () < A:
                infectados.append (j)
            # recuperação
            if random () < B:
                if modelo != 'si':
                    infectados.remove (i)
                if modelo == 'sir':
                    imunizados.append (i)
            
            resultado_infectados[it] += len (infectados) / len (G)
            resultado_recuperados[it] += len (imunizados) / len (G)
            resultado_suscetiveis[it] += 1 - (resultado_infectados[it] + resultado_recuperados[it])
    return [x / len (G) for x in resultado_infectados], [x / len (G) for x in resultado_suscetiveis], [x / len (G) for x in resultado_recuperados]

def reativo (G, modelo, iterações, A, B = 0, imunizados = []):
    resultado_infectados = [0] * iterações
    resultado_suscetiveis = [0] * iterações
    resultado_recuperados = [0] * iterações
    for nóInicial in G:
        infectados = [nóInicial]
        for it in range (iterações):
            i = choice (infectados)
            for j in filter (lambda x: not x in imunizados, G[i]):
                # recuperação do passo anterior (pra poder infectar denovo)
                if modelo == 'sis' and j in infectados and random () < B:
                    infectados.remove (j)
                # tenta infectar
                if random () < A:
                    infectados.append (j)
            # recuperação
            if random () < B:
                if modelo != 'si':
                    infectados.remove (i)
                if modelo == 'sir':
                    imunizados.append (i)
            resultado_infectados[it] += len (infectados) / len (G)
            resultado_recuperados[it] += len (imunizados) / len (G)
            resultado_suscetiveis[it] += 1 - (resultado_infectados[it] + resultado_recuperados[it])
    return [x / len (G) for x in resultado_infectados], [x / len (G) for x in resultado_suscetiveis], [x / len (G) for x in resultado_recuperados]
