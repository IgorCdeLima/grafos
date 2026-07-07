from interface.IGraph import IGraph
import random

class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso

class GKruskal(IGraph):

    def createrGraph(self):
        graph = []
        NodeList = list(range(1, 11))

        print("Grafo gerado:")
        print(f"(ORIGEM)\t(PESO)\t\t(DESTINO)")

        for i in range(len(NodeList)):
            for j in range(i + 1, len(NodeList)):
                graph.append(
                    Aresta(

                    origem = NodeList[i],
                    destino= NodeList[j],
                    peso = random.randint(1, 36)
                    )
                )
                    
        graph.sort(key=lambda x: x.peso)

        for iten in graph:
            print(f"  ({iten.origem:02d})\t---\t  {iten.peso:02d}\t---\t  ({iten.destino:02d})")

        print("\nGrafo criado com sucesso!\n\n")

        return {
            'graph':graph,
            'vertices':NodeList
        }
    