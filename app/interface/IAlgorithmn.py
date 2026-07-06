from abc import ABC, abstractmethod


class IAlgorithmn(ABC):

    @abstractmethod
    def run(graph):
        pass
    
    @abstractmethod
    def TDE():
        pass

    def save(graph):
        pass