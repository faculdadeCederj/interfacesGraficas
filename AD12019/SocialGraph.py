import DiGraph
import sys
commands = sys.argv[1]

# cria um grafo de amigos para uma rede social
class SocialGraph(DiGraph.DiGraph):
    def __init__(self, inputfile):
        super().__init__(self)

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
                        output.write(self.recommendFriends(arguments))


    def add(self, args):
        origin = args[0]
        dest = args[1]
        weight = args[2]

        originExists = False
        destExists = False

        for vertex in self.vertexSet:
            if origin == vertex.name:
                originExists = True
            
            if dest == vertex.name:
                destExists = True

        if originExists:
            origin = DiGraph.Vertex(origin)
            self.addVertex(origin)

        if destExists:
            dest = DiGraph.Vertex(dest)
            self.addVertex(dest)

        origin.addEdge(DiGraph.Edge(dest, weight))

        edgesNum = 0
        for vertex in self.vertexSet:
            edgesNum += len(vertex.edgesSet)

        return f'addEdge: (True) - {edgesNum} edges, {len(self.vertexSet)} vertices'
        

    def remove(self, args):
        vert = args[0]

        self.removeVertex(vert)

        edgesNum = 0
        for vertex in self.vertexSet:
            edgesNum += len(vertex.edgesSet)

        return f'addEdge: (True) - {edgesNum} edges, {len(self.vertexSet)} vertices'


    def showFriends(self, args):
        vertex = args[0]
        self.showEdges(vertex)

    def shortestPath(self, args):
        origin = args[0]
        dest = args[1]
        return self.Dijkstra(origin, dest)

    def recommendFriends(self, args):
        baseVertex = args[0]
        mesure = args[1]
        topK = args[2]
        return self.topVertex(baseVertex, mesure, topK)

if __name__ == '__main__':
    # running must be `python3 SocialGraph.py infile.txt`
    graph = SocialGraph(commands)