from interface.IGraph import IGraph
import random
import string



class GFloydWarshall(IGraph):

    def createrGraph(self):
        QTD_VERTICES = 5
        matriz = [[float('inf')] * QTD_VERTICES for _ in range(QTD_VERTICES)]
        m_next =  [[None] * QTD_VERTICES for _ in range(QTD_VERTICES)]

        NodeList = random.sample(string.ascii_uppercase, QTD_VERTICES)



        for linha in range(QTD_VERTICES ):
            for coluna in range(QTD_VERTICES):
                if linha == coluna:
                    matriz[linha][coluna] = 0
                    m_next[linha][coluna] = coluna

                elif random.choice([True, True, False, False]):
                    matriz[linha][coluna] = random.randint(1,20)
                    m_next[linha][coluna] = coluna



        return {
            'matriz': matriz,
            'vertices': NodeList,
            'next': m_next
        }