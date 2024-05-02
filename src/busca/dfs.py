def dfs(graph, start: int, goal: int) -> (int, float, [int]):
	#Validando a existência dos nós
	try:
		graph[start]
		graph[goal]
	except IndexError:
		print("Node doesn't exist")
		return None

	stack = list()
	stack.append((start, -1, 0))
	
	visitedNodes = list()
	
	while (len(stack)):
		nodeTuple = stack.pop()
		currNode, predecessor, weight = nodeTuple
		
		if goal == currNode:
			path = [currNode]
			totalCost = weight
			countNodes = 1
				
			while predecessor != -1 and len(visitedNodes):
				visitedNode, visitedNodePredecessor, visitedNodeWeight = next(filter(lambda v: v[0] == predecessor, visitedNodes))
				
				if predecessor == visitedNode:
					predecessor = visitedNodePredecessor
					totalCost += visitedNodeWeight
					path.append(visitedNode)

			path.reverse()
			return (len(path) - 1, totalCost, path)
			
		if not nodeTuple in visitedNodes:
			visitedNodes.append(nodeTuple)
			nodesVizinhos = graph[currNode][1].items()
			
			for nodeVizinho, pesoNodeVizinho in nodesVizinhos:
				if(nodeVizinho != predecessor):
					stack.append((nodeVizinho, currNode, pesoNodeVizinho))
