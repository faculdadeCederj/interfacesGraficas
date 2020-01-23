import DiGraph
import sys
#commands = sys.argv[1]

# TODO show commands in outfile before the results
# TODO create docfile using doxygen

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
                        output.write(self.add(arguments) + '\n')
                    elif command == 'remove':
                        output.write(self.remove(arguments) + '\n')
                    elif command == 'showFriends':
                        output.write(self.showFriends(arguments) + '\n')
                    elif command == 'shortestPath':
                        output.write(self.shortestPath(arguments) + '\n')
                    elif command == 'recommendFriends':
                        output.write(str(self.recommendFriends(arguments))+'\n')


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
            
            if dest == vertex.name:
                destExists = True
                destVert = vertex
                #exec(f'{dest} = DiGraph.Vertex(dest)')
                #exec(f'self.addVertex({dest})')

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
        
        if not edgeExists:
            originVert.addEdge(DiGraph.Edge(destVert, weight))
        #edge = DiGraph.Edge(dest, weight)   
        #exec(f'{origin}.addEdge(edge)')

        edgesNum = 0
        for vertex in self.vertexSet:
            edgesNum += len(vertex.edgesSet)

        return f'addEdge: (True) - {edgesNum} edges, {len(self.vertexSet)} vertices '
        

    def remove(self, args):
        vert = args[0]

        for vertex in self.vertexSet:
            if vertex.name == vert:
                vert = vertex
                break

        self.removeVertex(vert)

        edgesNum = 0 
        for vertex in self.vertexSet:
            edgesNum += len(vertex.edgesSet)

        return f'remove: (True) - {edgesNum} edges, {len(self.vertexSet)} vertices '


    def showFriends(self, args):
        vertex = args[0]

        for vert in self.vertexSet:
            if vert.name == vertex:
                vertex = vert

        return self.showEdges(vertex)

    def shortestPath(self, args): 
        origin = args[0]            
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
        topK = int(args[2])  

        for vert in self.vertexSet:
            if baseVertex == vert.name:
                baseVertex = vert
                break

        auxList = self.topVertex(baseVertex, mesure, topK)
        returnList = list()

        for vertex in auxList:
            if 'inf' in vertex:
                continue
            else:
                returnList.append(vertex)

        return returnList

if __name__ == '__main__':
    # running must be `python3 SocialGraph.py infile.txt`
    #graph = SocialGraph(commands)
    graph = SocialGraph('./AD12019/infile.txt')