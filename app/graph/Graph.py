import random
from interface.IGraph import IGraph

class Node:
    def __init__(self, value):
        self.data = value
        self.vizinhos = []



class Graph(IGraph):


    def createrGraph(self):
        number = random.sample(range(1, 20), 5)
        NodeList = [Node(n) for n in number]

        print("Grafo gerado:")
        for node in NodeList:
            for newNode in NodeList:
                if node != newNode and (random.choice([True, False, False, False, False])):
                    print(f"({node.data:02d}) <-> ({newNode.data:02d})")
                    node.vizinhos.append(newNode)
                    if random.choice([True, False]):
                        newNode.vizinhos.append(node)


        self.initial_graph = NodeList[0]

        return self.initial_graph
