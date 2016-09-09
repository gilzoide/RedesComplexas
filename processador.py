## Processador dos grafo ##

from os import makedirs
import networkx as nx

def criaPastaSaída (entrada):
    """Cria a pasta de saída (se precisar) baseado no nome da entrada, e retorna
    o nome da pasta"""
    nome = entrada.replace ('in', 'out')
    # tenta criar pasta
    try:
        makedirs (nome)
    except Exception as ex:
        pass

    return nome


def processa (nomeEntrada):
    """Processa arquivo da rede, pondo as saídas na pasta com o nome 'out/<rede>'
    Saídas:
        - ?
    """
    # lê o arquivo de entrada
    G = nx.read_edgelist (nomeEntrada, nodetype = int, comments = '%')
    # e acha o maior componente
    G = max (nx.connected_component_subgraphs (G), key = len)

    nomeRede = criaPastaSaída (nomeEntrada)
