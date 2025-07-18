from typing import TypeVar, Generic

from .engines import get_engine

T = TypeVar('T')

class Calculator(Generic[T]):
    """
    A simple calculator for octonions.
    """
    
    def __init__(self, engine_name: str):
        """
        Initialize the calculator with the specified engine.
        
        :param engine_name: Name of the engine to use.
        """
        self.engine = get_engine(engine_name)

    def __repr__(self):
        """
        String representation of the calculator.
        
        :return: String representation of the engine.
        """
        engine = repr(self.engine)
        return f"Calculator using engine: {engine}"

    def add(self, a: T, b: T) -> T:
        """
        Add two complex numbers using the engine.
        
        :param a: First complex number.
        :param b: Second complex number.
        :return: Resulting octonion after addition.
        """
        return self.engine.add(a, b)
    
    def subtract(self, a: T, b: T) -> T:
        """
        Subtract two complex numbers using the engine.
        
        :param a: First complex number.
        :param b: Second complex number.
        :return: Resulting octonion after subtraction.
        """
        return self.engine.subtract(a, b)
    
    def multiply(self, a: T, b: T) -> T:
        """
        Multiply two complex numbers using the engine.
        
        :param a: First complex number.
        :param b: Second complex number.
        :return: Resulting octonion after multiplication.
        """
        return self.engine.multiply(a, b)

    def division(self, a: T, b: T) -> T:
        """
        Divide two complex numbers using the engine.
        
        :param a: First complex number.
        :param b: Second complex number.
        :return: Resulting octonion after division.
        """
        return self.engine.division(a, b)
    
    def conjugate(self, a: T) -> T:
        """
        Calculate the conjugate of a complex number using the engine.
        """
        return self.engine.conjugate(a)
    
    def inverse(self, a: T) -> T:
        """
        Calculate the inverse of a complex number using the engine.
        
        :param a: Complex number to invert.
        :return: Inverse of the complex number.
        """
        return self.engine.inverse(a)