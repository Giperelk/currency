from abc import ABC, abstractmethod


class ABCWriter(ABC):

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def write_detail(self):
        pass
