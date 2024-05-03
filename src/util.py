"""Funções auxiliares para o projeto"""

import math


def haversine(lat1, lon1, lat2, lon2):
    """Calcula a distância, em metros, entre duas coordenadas GPS."""
    dLat = (lat2 - lat1) * math.pi / 180.0  # pylint: disable=invalid-name
    dLon = (lon2 - lon1) * math.pi / 180.0  # pylint: disable=invalid-name
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
    # apply formulae
    a = (
        pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
        math.cos(lat1) * math.cos(lat2)
    )
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return (rad * c)*1000


#
# Não altere este comentário e adicione suas funções ao final do arquivo.
#

def manhattan(graph, a, b):
    """Heurística de Manhattan, usada como estimativa para o valor da aresta que une dois vértices"""
    try:
        a, b = graph.nodes[a], graph.nodes[b]
    except KeyError:
        raise Exception('Não foi possível achar os nodos para os valores a e b - Manhattan - A*')
    return abs(a['lat'] - b['lat']) + abs(a['lon'] - b['lon'])
