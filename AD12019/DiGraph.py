#classe do digrafo
class DiGraph:
    def __init__(self, vertexSet=set()):
        self.vertexSet = set()
        for name in vertexSet:
            name = self.Vertex(name)
            self.vertexSet.add(self.Vertex(name))

    def showDigraph(self):
        print('<', end=' ')
        for vertex in self.vertexSet:
            print(vertex.name, end=' ')
        print('>')
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
                djikstraPath.append(vertexDest)
                nextVertex = prev[vertexDest]
                while nextVertex != None:
                    djikstraPath.append(nextVertex)
                    nextVertex = prev[nextVertex]
                djikstraPath = djikstraPath[::-1]
                return djikstraPath


    def topVertex(self, vertex, mesure, topK):
        if mesure == 'dist':
            pass
        if mesure == 'weightedDist':
            pass

    # classe cria o objeto vertice
    class Vertex:
        def __init__(self, name, edgesSet=set()):
            self.name = name
            self.edgesSet = edgesSet

        def addEdge(self, vertex, weight=1):
            if vertex in super.vertexSet:
                edge = self.Edge(vertex, weight)
                self.edgesSet.add(edge)
            else:
                print('invalid vertex')


        def __str__(self):
            edgeString = ''
            for edge in self.edgesSet:
                if edgeString == '':
                    edgeString += f'{edge.__str__()}'
                else:
                    edgeString += f', {edge.__str__()}'
            edgeString = '{' + edgeString + '}'
            return edgeString

        # classe de arestas
        class Edge:
            def __init__(self, vertex, weight=1):
                self.weight = weight
                self.vertex = vertex
            
            def __str__(self):
                return f'<{self.vertex.name}, {self.weight}>'


if __name__ == '__main__':
    vertices = {'joao', 'rogerio', 'maria'}
    digrafo = DiGraph(vertices)
    digrafo.showDigraph()
    digrafo..addEdge(3, )