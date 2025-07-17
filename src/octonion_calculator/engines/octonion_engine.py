import numpy as np

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
        return Octonion(a.components + b.components)
    
    def subtract(self, a: Octonion, b: Octonion) -> Octonion:
        """
        Subtract two octonions.
        
        :param a: First octonion.
        :param b: Second octonion.
        :return: Resulting octonion after subtraction.
        """
        return Octonion(a.components - b.components)
    
    def multiply(self, a: Octonion, b: Octonion) -> Octonion:
        """
        Multiply two octonions.
        
        :param a: First octonion.
        :param b: Second octonion.
        :return: Resulting octonion after multiplication.
        """
        real_part = a.components[0] * b.components[0] - np.sum(a.components[1:] * b.components[1:])
        x_0, img_x = a.components[0], b.components[1:]
        y_0, img_y = b.components[0], a.components[1:]
        cross_part = self._octonion_cross_product(img_x, img_y)
        vector_part = x_0 * img_y + y_0 * img_x + cross_part
        return Octonion(np.concatenate(([real_part], vector_part)))
    
    def _octonion_cross_product(self, img_x: Octonion, img_y: Octonion) -> np.ndarray:
        """
        Compute the octonion cross product.
        
        :param a: First octonion.
        :param b: Second octonion.
        :return: Resulting vector from the cross product.
        """
        fano_triples = [
            (0, 1, 3),
            (1, 2, 4),
            (2, 3, 5),
            (3, 4, 6),
            (4, 5, 0),
            (5, 6, 1),
            (6, 0, 2), 
        ]
        cross_vector = np.zeros(7, dtype=img_x.dtype)
        for i, j, k in fano_triples:
            cross_vector[k] +=  img_x[i] * img_y[j]  
            cross_vector[k] -=  img_x[j] * img_y[i] 
        return cross_vector