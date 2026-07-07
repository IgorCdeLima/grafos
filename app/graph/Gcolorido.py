from interface.IGraph import IGraph
import random
import string

class Node:
    def __init__(self,data):
        self.data = data
        self.cor = None
        self.grau = 0
        self.vizinho = []


class Gcolorido(IGraph):

    def createrGraph(self):
        QTD_VERTICES = 10
        
        cores = self.gerarCor()

        datas = random.sample(string.ascii_uppercase, QTD_VERTICES)

        NodeList = [Node(datas[i]) for i in range(QTD_VERTICES)]

        zoologicoNodes = [Node(datas[i]) for i in range(QTD_VERTICES)]
        
        self.gerarVizinho(NodeList)
        NodeList.sort(key=lambda node: node.grau, reverse=True)

        zoologico = self.graphZoo(zoologicoNodes)

        return {
            'graph': NodeList,
            'cores': cores,
            'zooGraph': zoologico
        }
        

    def gerarCor(self):
        numero = {}
        for num in range(10):
            numero[num] = ("#{:06X}".format(random.randint(0, 0xFFFFFF)))
        return numero
        
    def gerarVizinho(self, nodeList):

        for node in nodeList:
            for _ in range(random.randint(1,len(nodeList)-1)):
                value = random.randint(0,len(nodeList)-1)
                newVizinho = nodeList[value]
                if newVizinho not in node.vizinho and newVizinho != node:
                    node.vizinho.append(newVizinho)
                    newVizinho.vizinho.append(node)
                    node.grau +=1
                    newVizinho.grau +=1

    def graphZoo(self, graph):

        graph[0].vizinho.append(graph[2])
        graph[0].grau +=1

        graph[1].vizinho.append(graph[3])
        graph[1].grau +=1

        graph[2].vizinho.append(graph[0])
        graph[2].vizinho.append(graph[3])
        graph[2].grau +=2

        graph[3].vizinho.append(graph[1])
        graph[3].vizinho.append(graph[2])
        graph[3].grau += 2

        graph[4].vizinho.append(graph[5])
        graph[4].vizinho.append(graph[9])
        graph[4].grau +=2


        graph[5].vizinho.append(graph[4])
        graph[5].vizinho.append(graph[6])
        graph[5].grau +=2

        graph[6].vizinho.append(graph[5])
        graph[6].vizinho.append(graph[7])
        graph[6].vizinho.append(graph[9])
        graph[6].grau +=3

        graph[7].vizinho.append(graph[6])
        graph[7].vizinho.append(graph[8])
        graph[7].grau +=2

        graph[8].vizinho.append(graph[7])
        graph[8].vizinho.append(graph[9])
        graph[8].grau +=2

        graph[9].vizinho.append(graph[4])
        graph[9].vizinho.append(graph[6])
        graph[9].vizinho.append(graph[8])
        graph[9].grau +=3

        return graph