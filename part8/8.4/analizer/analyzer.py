from abc import ABC, abstractmethod


class Analyzer(ABC):

    @abstractmethod
    def run(self) -> None:
        ...