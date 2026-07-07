from interface.IGraph import IGraph
import random
import string


class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso

class GDijkstra(IGraph):

    def createrGraph(self):
        graph = []
        NodeList = random.sample(string.ascii_uppercase, 10)

        
        print("Grafo gerado:")
        print(f"(ORIGEM)\t(PESO)\t\t(DESTINO)")

        for i in range(len(NodeList)):
            for j in range(i + 1, len(NodeList)):
                if random.choice([True, True, True, True, False]):
                    graph.append(
                        Aresta(
                        origem = NodeList[i],
                        destino= NodeList[j],
                        peso = random.randint(1, 36)
                        )
                    )
                        
        graph.sort(key=lambda x: x.peso)

        for iten in graph:
            print(f"  ({iten.origem})\t---\t  {iten.peso:02d}\t--->\t  ({iten.destino})")



        print("\nGrafo criado com sucesso!\n\n")

        lista_ajd = {}

        for v in NodeList:
            lista_ajd[v] = []
        
        for aresta in graph:
            lista_ajd[aresta.origem].append((aresta.destino, aresta.peso))

        print("\nLista de adjsascencia:\n")
        for iten in lista_ajd:
            print(f"({iten}): {lista_ajd[iten]}")
        print("\nLista gerada!\n")

        return {
            'adj':lista_ajd,
            'vertices':NodeList,
        }