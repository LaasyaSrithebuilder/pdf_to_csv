from abc import ABC, abstractmethod

class TextExtractor(ABC):
    @abstractmethod
    def extract(self, source: str) -> str:
        pass

class TransactionParser(ABC):
    @abstractmethod
    def parse(self, text: str) -> list:
        pass

class CustomerParser(ABC):
    @abstractmethod
    def parse(self, text: str) -> dict:
        pass