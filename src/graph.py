def read_graph(filename):
    grafo = {}
    with open(filename, 'r') as file:
        content = file.readlines()
        content = [line.strip('\n').split() for line in content]
        contentConvertedToNumbers = []
        for i in content:
            line = []
            for j in i:
                if('.' in j):
                    line.append(float(j))
                else:
                    line.append(int(j))
            contentConvertedToNumbers.append(line)
        numberOfNodes = contentConvertedToNumbers[0][0]
        nodeDescription = contentConvertedToNumbers[1:(numberOfNodes + 1)]
        for i in nodeDescription:
            for j in i:
                grafo.update({nodeDescription[j][0]: [[nodeDescription[j][1], nodeDescription[j][2]], {}]})
                break
        vertexDescription = contentConvertedToNumbers[(numberOfNodes + 2):]
        cont = 0
        for i in vertexDescription:
            for j in i:
                grafo[j][1].update({vertexDescription[cont][1]: vertexDescription[cont][2]})
                grafo[i[1]][1].update({i[0]: i[2]})
                break
            cont = cont + 1
    return grafo