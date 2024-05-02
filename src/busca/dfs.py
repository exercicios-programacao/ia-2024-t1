def dfs(graph, start: int, goal: int) -> (int, float, [int]):
	#Validando a existência dos nós
 
	try:
		graph[start]
		graph[goal]
	except IndexError:
		print("Node doesn't exist")
		return None

	stack = [(start, None)]
	visitedNodes = {}
	
	while len(stack):
		currNode, predecessor = stack.pop()
		
		if goal == currNode:
			path = [currNode]
			totalCost = 0
				
			while predecessor is not None:
				path.append(predecessor)
				totalCost += graph[predecessor][1][currNode]
				currNode = predecessor
				predecessor = visitedNodes.get(currNode)

			path.reverse()
			return (len(path) - 1, totalCost, path)

		if currNode not in visitedNodes:
			visitedNodes[currNode] = predecessor

			for neighbor, cost in graph[currNode][1].items():
				if neighbor not in visitedNodes:
					stack.append((neighbor, currNode))
