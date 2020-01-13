# classe de arestas
class Edge:
    def __init__(self, vertex, weight=1):
        self.weight = weight
        self.vertex = vertex
    
    def __str__(self):
        return f'<{self.vertex.name}, {self.weight}>'



# classe cria o objeto vertice
class Vertex:
    def __init__(self, name):
        edgesSet = set()
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
                djikstraPath.append(vertexDest)
                nextVertex = prev[vertexDest]
                while nextVertex != None:
                    djikstraPath.append(nextVertex)
                    nextVertex = prev[nextVertex]
                djikstraPath = djikstraPath[::-1]

        # formatando saida
        returnStr = '['
        for vert in djikstraPath:
            returnStr += f'<{vert.name}, {cost[vert]}>,'
        returnStr = returnStr[:-1]
        returnStr += ']'

        return returnStr

    def topVertex(self, baseVertex, mesure, topK):
        costs = dict()
        for vertex in self.vertexSet:
            if vertex == baseVertex:
                costs[vertex.name] = 0
            else:
                costs[vertex.name] = float('inf')

        def calculateCost(vert):
            for edge in vert.edgesSet:
                calc = costs[vert.name] + edge.weight
                if calc < costs[edge.vertex.name]:
                    costs[edge.vertex.name] = calc
                calculateCost(edge.vertex)
        
        calculateCost(baseVertex)

        if mesure == 'weightedDist':
            totalEdges = 0
            toplist = list() 
            edgesScore = dict()

            for vertex in self.vertexSet:
                edgesScore[vertex.name] = 0
          
            for vertex in self.vertexSet:
                totalEdges += len(vertex.edgesSet)

                for edge in vertex.edgesSet:
                    edgesScore[edge.vertex.name] += 1

            # multiply costs by total edges and removing edges num 
            for vertex, cost in costs.items():
                vertEdgesScore = edgesScore[vertex]
                costs[vertex] = cost*totalEdges-vertEdgesScore

        # remove neighbors and base
        for edge in baseVertex.edgesSet:
            costs.pop(edge.vertex.name)
        costs.pop(baseVertex.name)

        toplist = list()
        while topK != 0:
            smaller = float('inf')
            topVert = None
            for vertex, cost in costs.items():
                if cost <= smaller:
                    smaller = cost
                    topVert = vertex
            toplist.append(f'{topVert}:{smaller}')
            costs.pop(topVert)
            topK -= 1
        return toplist
                


if __name__ == '__main__':
    joao = Vertex('joao')
    pedro = Vertex('pedro')
    julia = Vertex('julia')
    rosicreida = Vertex('rosicreida')
    ana = Vertex('ana')
    luis = Vertex('luis')
    vertices = {joao, pedro, julia, rosicreida, ana, luis}
    
    joao.addEdge(Edge(pedro, 2))
    joao.addEdge(Edge(ana, 3))
    joao.addEdge(Edge(julia, 1))
    
    pedro.addEdge(Edge(ana, 1))

    ana.addEdge(Edge(rosicreida, 1))

    rosicreida.addEdge(Edge(luis, 3))

    julia.addEdge(Edge(rosicreida, 1))

    digrafo = DiGraph(vertices)
    digrafo.showEdges(joao)
##########################################

    joaquina = Vertex('joaquina')
    digrafo.addVertex(joaquina)
    print('inserindo joaquina: ', end=' ')
    for vertex in digrafo.vertexSet:
        print(vertex.name, end=' ')
    print()

    digrafo.removeVertex(joaquina)
    print('tirando joaquina: ', end=' ')
    for vertex in digrafo.vertexSet:
        print(vertex.name, end=' ')
    print()

###########################################

    dji = digrafo.Dijkstra(joao, luis)
    print('dijkstra joao >>> luis:', end=' ')
    print(dji)

###########################################

    print(digrafo.topVertex(joao, 'dist', 2))

############################################

    print(digrafo.topVertex(joao, 'weightedDist', 2))