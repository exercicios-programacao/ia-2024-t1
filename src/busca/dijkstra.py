"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from queue import PriorityQueue
from heapq import heappush, heappop, heapify
from util import haversine


def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    nodesQueue = []
    processedNodes = []
    tempNodes = {}
    heappush(nodesQueue, (0, start))

    tempNodes[start] = {
        'predecessor': None,
        'currWeight': 0,
        'allPredecessors': [None]
    }

    while nodesQueue:
        weight, node = heappop(nodesQueue)

        if(node in processedNodes):
            continue
            
        processedNodes.append(node)
        print("nó atual",node)
        if(node == goal):
            totalWeight = tempNodes[node]['currWeight']
            path = [goal]
            currentPathNode = goal

            while(path[-1] != start):
                predecessor = tempNodes[currentPathNode]['predecessor']
                currentPathNode = predecessor
                path.append(predecessor)

            path.reverse()
            return (len(processedNodes), totalWeight, path)
        
        visitedNode = tempNodes[node] 
        for neighborNode, neighborNodeWeight in graph[node][1].items():
            if(neighborNode not in tempNodes or node not in tempNodes[neighborNode]['allPredecessors']):
                newWeight = visitedNode['currWeight'] + neighborNodeWeight
                newPredecessor = node

                if (neighborNode not in tempNodes):
                    heappush(nodesQueue, (newWeight, neighborNode))
                    tempNodes[neighborNode] = {
                        'predecessor': newPredecessor,
                        'currWeight': newWeight,
                        'allPredecessors': [newPredecessor]
                    }
                elif (newWeight < tempNodes[neighborNode]['currWeight']):
                    heappush(nodesQueue, (newWeight, neighborNode))
                    newAllPredecessors = tempNodes[neighborNode]['allPredecessors']
                    newAllPredecessors.append(newPredecessor)

                    tempNodes[neighborNode] = {
                        'predecessor': newPredecessor,
                        'currWeight': newWeight,
                        'allPredecessors': newAllPredecessors
                    }
                else:
                    tempNodes[neighborNode]['allPredecessors'].append(newPredecessor)
