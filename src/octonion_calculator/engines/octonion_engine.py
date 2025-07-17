from .base_engine import BaseEngine
from ..models.octonion import Octonion

class OctonionEngine(BaseEngine[Octonion]):
    """
    Engine for performing operations on octonions.
    """

    def __init__(self):
        """
        Initialize the octonion engine.
        """

    def __repr__(self):
        """
        String representation of the octonion engine.
        """
        return "OctonionEngine()"

    def add(self, a: Octonion, b: Octonion) -> Octonion:
        """
        Add two octonions.
        
        :param a: First octonion.
        :param b: Second octonion.
        :return: Resulting octonion after addition.
        """
        return a + b
