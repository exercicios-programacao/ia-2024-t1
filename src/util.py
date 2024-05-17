"""Funções auxiliares para o projeto."""

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

def mountpath(visited_nodes, curr_node, predecessor, graph):
    """Monta o path do caminho encontrado."""
    path = [curr_node]
    total_cost = 0

    while predecessor is not None:
        path.append(predecessor)
        total_cost += graph[predecessor][1][curr_node]
        curr_node = predecessor
        predecessor = visited_nodes.get(curr_node)

    path.reverse()

    return (path, total_cost)
