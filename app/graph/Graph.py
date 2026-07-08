import random
from interface.IGraph import IGraph

class Node:
    def __init__(self, value):
        self.data = value
        self.vizinhos = []



class Graph(IGraph):


    def createrGraph(self):
        number = random.sample(range(1, 20), 10)
        NodeList = [Node(n) for n in number]

        print("Grafo gerado:")
        print("(ORIGEM)-->\t(DESTINO)\n")

        for node in NodeList:
            for newNode in NodeList:
                if node != newNode and (random.choice([True, False, False, False, False])):
                    print(f"({node.data:02d})\t-->\t({newNode.data:02d})")
                    node.vizinhos.append(newNode)
                    if random.choice([True, False, False]):
                        print(f"({newNode.data:02d})\t-->\t({node.data:02d})")
                        newNode.vizinhos.append(node)


        self.initial_graph = NodeList[0]

        print("\nGrafo criado com sucesso!\n\n")
        return self.initial_graph
