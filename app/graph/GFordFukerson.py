from interface.IGraph import IGraph
import random
import string

class Vertices:
    def __init__(self, data, tipo = None):
        self.data = data
        self.tipo = tipo
        self.arestas = []

class Aresta:
    def __init__(self, destino, capacidade = 1):
        self.destino = destino
        self.capacidade = capacidade
        self.fluxo = 0


class GFordFukerson(IGraph):

    def createrGraph(self):
        QTD_VERTICES = 10

        datas = random.sample(string.ascii_uppercase, QTD_VERTICES)


        nodeList = [Vertices(datas[i]) for i in range(QTD_VERTICES)]
        arestaList = []

        source = Vertices('SINK', 'SINK')
        sink = Vertices('EXIT', 'EXIT')


        for _ in range(0, QTD_VERTICES):
            vertice_aleatorio = random.randint(0,QTD_VERTICES-1)

            arestaList.append(
                    Aresta(
                        destino = nodeList[vertice_aleatorio],
                    )
            )
        
        for node in nodeList:
            for aresta in arestaList:
                if (random.choice([True, False])) and (aresta.destino != node) and (self.verifivarAresta(node.arestas, aresta)):
                    aresta.capacidade = random.randint(1,20)
                    node.arestas.append(aresta)
        
        for aresta in arestaList:
            if random.choice([True, False, False, False, False]) and aresta.destino != sink:
                aresta.capacidade = random.randint(1,20)
                source.arestas.append(aresta)

        for _ in range(1, 2 ):
            arestaNum = random.randint(0,QTD_VERTICES-1)
            arestaList[arestaNum].capacidade =  random.randint(1,20)
            arestaList[arestaNum].destino = sink
    
    
        for node in nodeList:
            lista = []
            for aresta in node.arestas:
                if self.verifivarAresta(lista, aresta):
                    lista.append(aresta)

            node.arestas = lista

        return {
            'source': source,
            'sink': sink,
            'nodeList': nodeList,
            'arestaList': arestaList
        }


    def verifivarAresta(self, listaArestas, aresta):
        nao_presente = True
        for A in listaArestas:
            if A.destino == aresta.destino:
                nao_presente = False

        return nao_presente