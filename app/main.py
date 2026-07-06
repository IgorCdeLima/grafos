from utils.contracts import Contracts

    
if __name__ == '__main__':

    name_algorithmn = 'BFS'

    algorithm = Contracts.get_algorithm(name_algorithmn)
    graph = Contracts.get_graph(name_algorithmn).createrGraph()
    algorithm.save(graph)
    algorithm.run(algorithm.graph)
    algorithm.TDE()

