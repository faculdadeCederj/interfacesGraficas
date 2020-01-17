import DiGraph
import sys
#commands = sys.argv[1]

# cria um grafo de amigos para uma rede social
class SocialGraph(DiGraph.DiGraph):
    def __init__(self, inputfile):
        self.vertexSet = set()
        super().__init__(self.vertexSet)

        # opening the inputfile and writing the output in outfile
        with open(inputfile, 'r') as input:
            for line in input:
                allcommand = line.split()
                command = allcommand[0]
                allcommand.pop(0)
                arguments = allcommand
                with open('outfile.txt', 'a') as output:
                    if command == 'add':
                        output.write(self.add(arguments))
                    elif command == 'remove':
                        output.write(self.remove(arguments))
                    elif command == 'showFriends':
                        output.write(self.showFriends(arguments))
                    elif command == 'shortestPath':
                        output.write(self.shortestPath(arguments))
                    elif command == 'recommendFriends':
                        output.write(str(self.recommendFriends(arguments)))


    def add(self, args):
        origin = args[0]
        dest = args[1]
        weight = int(args[2])

        # TODO fix issue in doubled vertex and empty edges set
        
        originExists = False
        destExists = False

        for vertex in self.vertexSet:
            if origin == vertex.name:
                originExists = True
                originVert = vertex
                #exec(f'{origin} = DiGraph.Vertex(origin)')
                #exec(f'self.addVertex({origin})')
                break
            
            if dest == vertex.name:
                destExists = True
                destVert = vertex
                #exec(f'{dest} = DiGraph.Vertex(dest)')
                #exec(f'self.addVertex({dest})')
                break

        if not originExists:
            originVert = DiGraph.Vertex(origin)
            self.addVertex(originVert)
            #exec(f'{origin} = DiGraph.Vertex(origin)')
            #exec(f'self.addVertex({origin})')

            


        if not destExists:
            destVert = DiGraph.Vertex(dest)
            self.addVertex(destVert)
            #exec(f'{dest} = DiGraph.Vertex(dest)')
            #exec(f'self.addVertex({dest})')

        edgeExists = False
        for edge in originVert.edgesSet:
            if edge.vertex.name == dest:
                edgeExists = True
                edge.weight = weight
                break
        
        if edgeExists:
            originVert.addEdge(DiGraph.Edge(destVert, weight))
        #edge = DiGraph.Edge(dest, weight)   # TODO fix edge dest is a string not a vertex 
        #exec(f'{origin}.addEdge(edge)')

        edgesNum = 0
        for vertex in self.vertexSet:
            edgesNum += len(vertex.edgesSet)

        return f'addEdge: (True) - {edgesNum} edges, {len(self.vertexSet)} vertices'
        

    def remove(self, args):
        vert = args[0]

        for vertex in self.vertexSet:
            if vertex == vert:
                vert = vertex
                break

        self.removeVertex(vert)

        edgesNum = 0
        for vertex in self.vertexSet:
            edgesNum += len(vertex.edgesSet)

        return f'addEdge: (True) - {edgesNum} edges, {len(self.vertexSet)} vertices'


    def showFriends(self, args):
        vertex = args[0]
        return self.showEdges(vertex)

    def shortestPath(self, args): # TODO fix data structures work between shortestPath and Dijkstra
        origin = args[0]          # problems in dijkstra ln 61-79 with near variable and edges sets  
        dest = args[1]

        vertDict = dict()

        for vertex in self.vertexSet:
            vertDict[vertex.name] = vertex

        origin = vertDict[origin]
        dest = vertDict[dest]

        return self.Dijkstra(origin, dest)

    def recommendFriends(self, args):
        baseVertex = args[0]
        mesure = args[1]
        topK = int(args[2]) # TODO fix edge.vertex.name call, calls a str without attr name 

        for vert in self.vertexSet:
            if baseVertex == vert.name:
                baseVertex = vert
                break

        return self.topVertex(baseVertex, mesure, topK)

if __name__ == '__main__':
    # running must be `python3 SocialGraph.py infile.txt`
    #graph = SocialGraph(commands)
    graph = SocialGraph('./AD12019/infile.txt')