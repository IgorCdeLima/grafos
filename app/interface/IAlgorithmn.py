from abc import ABC, abstractmethod


class IAlgorithmn(ABC):

    @abstractmethod
    def run():
        pass
    
    @abstractmethod
    def TDE():
        pass

    def save(graph):
        pass