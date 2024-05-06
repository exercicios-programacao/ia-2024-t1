"""Funções auxiliares para o projeto"""

import json
import math
import sys


def haversine(lat1, lon1, lat2, lon2):
    """Calcula a distância, em metros, entre duas coordenadas GPS."""
    dLat = (lat2 - lat1) * math.pi / 180.0  # pylint: disable=invalid-name
    dLon = (lon2 - lon1) * math.pi / 180.0  # pylint: disable=invalid-name
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
    # apply formulae
    a = pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(
        lat1
    ) * math.cos(lat2)
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return (rad * c) * 1000


#
# Não altere este comentário e adicione suas funções ao final do arquivo.
#


def makeDict(graph):
    """usada no dijkstra para criar um dicionário com os pontos do grafo e seus visinhos e custos"""
    dict = {}
    for ponto in range(len(graph)):
        dictVisinhos = {}
        for visinho in graph[ponto][1]:
            dictVisinhos[visinho[0]] = visinho[1]
        x = float(graph[ponto][0][0])
        y = float(graph[ponto][0][1])
        dict[ponto] = {
            "posicao": {"x": x, "y": y},
            "visinhos": dictVisinhos,
            "custo": sys.maxsize,
            "anteriores": [],
        }
    return dict


def makeDict2(graph, goal):
    """usada no a_star para criar um dicionário com os pontos do grafo e seus visinhos e custos e distância até o goal que é a heuristica q eu vou usar"""
    dict = {}
    goalPos = graph[goal][0]
    for ponto in range(len(graph)):
        goalDistance = haversine(
            float(graph[ponto][0][0]),
            float(graph[ponto][0][1]),
            float(goalPos[0]),
            float(goalPos[1]),
        )
        dictVisinhos = {}
        for visinho in graph[ponto][1]:
            dictVisinhos[visinho[0]] = visinho[1]
        x = float(graph[ponto][0][0])
        y = float(graph[ponto][0][1])
        dict[ponto] = {
            "posicao": {"x": x, "y": y},
            "visinhos": dictVisinhos,
            "custo": float("inf"),
            "anteriores": [],
            "goalDistance": goalDistance,
        }
    # print(json.dumps(dict, indent=4))
    return dict
