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

    def Dijkstra(self, vertexBase, vertexDest):
        #criando listas para uso do algoritmo
        unvisited = self.vertexSet.copy()
        prev = dict()
        cost = dict()
        
        for vertex in unvisited:
            prev[vertex] = None
            
            if vertex == vertexBase:
                cost[vertex] = 0
            else:
                cost[vertex] = float('inf')

        # loop sobre lista dos nos nao visitados
        # para verificar o menor caminho
            while len(unvisited) != 0:

                # obtendo o no de menor custo e colocando em near
                smaller = float('inf')
                for vertex in unvisited:
                    if cost[vertex] < smaller:
                        near = vertex
                        smaller = cost[vertex]
                unvisited.remove(near)

                # usando as arestas do no de menor custo para 
                # visitar seus vizinhos
                for edge in near.edgesSet:
                    totalcost = cost[near] + edge.weight
                    if totalcost < cost[edge.vertex]:
                        cost[edge.vertex] = totalcost
                        prev[edge.vertex] = near
                
                # verificando se o no de menor custo é o destino
                # para retornar o menor caminho caso seja
                if near == vertexDest:
                    djikstraPath = list()
                    djikstraPath[vertexDest]
                    nextVertex = prev[vertexDest]
                    while nextVertex != None:
                        djikstraPath[nextVertex]
                        nextVertex = prev[nextVertex]
                    djikstraPath = djikstraPath[::-1]
                    return djikstraPath


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

print('\n')
digrafo = DiGraph({ vertice, vertice2, vertice3 })

print(digrafo.Dijkstra(vertice, vertice3))