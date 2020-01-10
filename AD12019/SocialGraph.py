import DiGraph
import sys
commands = sys.argv[1]

# cria um grafo de amigos para uma rede social
class SocialGraph(DiGraph.DiGraph):
    def __init__(self, inputfile):
        super().__init__(self)
        with open(inputfile, 'r') as input:
            for line in input:
                allcommand = line.split()
                command = allcommand[0]
                allcommand.pop(0)
                arguments = ''
                for argument in allcommand:
                    arguments += argument + ','
                arguments = arguments[:-1]
                with open('outfile.txt', 'a') as output:
                    output.write(self.command(arguments))



    def add(self):
        pass

    def remove(self):
        pass

    def showFriends(self):
        pass

    def shortestPath(self):
        pass

    def recommendFriends(self, dist=None, weightedDist=None):
        pass

if __name__ == '__main__':
    graph = SocialGraph(commands)