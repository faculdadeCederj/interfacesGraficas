# classe de arestas
class Edge:
    def __init__(self, vertex, weight=1):
        self.weight = weight
        self.vertex = vertex
    
    def __str__(self):
        return f'<{self.vertex.name}, {self.weight}>'



# classe cria o objeto vertice
class Vertex:
    def __init__(self, name, edgesSet=set()):
        self.name = name
        self.edgesSet = edgesSet

    def addEdge(self, edge):
        if 'Edge' in str(type(edge)):
            self.edgesSet.add(edge)
        else:
            print(f'type error: {type(edge)}')


    def __str__(self):
        edgeString = ''
        for edge in self.edgesSet:
            if edgeString == '':
                edgeString += f'{edge.__str__()}'
            else:
                edgeString += f', {edge.__str__()}'
        edgeString = '{' + edgeString + '}'
        return edgeString


#classe do digrafo
class DiGraph:
    def __init__(self, vertexSet=set()):
        self.vertexSet = vertexSet

    def showEdges(self, vertex):
        print(vertex)

    def addVertex(self, vertex):
        if 'Vertex' in str(type(vertex)):
            self.vertexSet.add(vertex)
        else:
            print(f'type error: {type(vertex)}')

    def removeVertex(self, vertex):
        if 'Vertex' in str(type(vertex)):
            self.vertexSet.remove(vertex)

    def shortestPath(self, vertexBase, vertexDest):
        pass



    def topVertex(self, vertex, mesure, topK):
        if mesure == 'dist':
            pass
        if mesure == 'weightedDist':
            pass

if __name__ == '__main__':
    vertice = Vertex('vertice')
    vertice2 = Vertex('vertice2')
    vertice3 = Vertex('vertice3')
    aresta = Edge(vertice2, 4)
    aresta2 = Edge(vertice3, 2)
    vertice.addEdge(aresta)
    digrafo = DiGraph({ vertice, vertice2 })
    digrafo.showEdges(vertice)
    digrafo.addVertex(vertice3)
    vertice.addEdge(aresta2)
    digrafo.showEdges(vertice)
    digrafo.removeVertex(vertice3)
for vertex in digrafo.vertexSet:
    print(vertex)