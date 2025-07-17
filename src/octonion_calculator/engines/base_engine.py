from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseEngine(ABC, Generic[T]):
    """
    Abstract class for all engines
    """
    def __init__(self):
        """
        Initialize the engine
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        String representation of the engine
        """
        pass

    @abstractmethod
    def add(self, a: T, b: T) -> T:
        """
        Add two octonions
        """
        pass
    
    @abstractmethod
    def subtract(self, a: T, b: T) -> T:
        """
        Subtract two octonions
        """
        pass
    
    @abstractmethod
    def multiply(self, a: T, b: T) -> T:
        """
        Multiply two octonions
        """
        pass