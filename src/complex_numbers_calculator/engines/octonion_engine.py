import numpy as np

from .complex_number_engine import CompexNumberEngine
from ..models.octonion import Octonion

class OctonionEngine(CompexNumberEngine[Octonion]):
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
    
    def multiply(self, a: Octonion, b: Octonion) -> Octonion:
        """
        Multiply two octonions.
        
        :param a: First octonion.
        :param b: Second octonion.
        :return: Resulting octonion after multiplication.
        """
        real_part = a.components[0] * b.components[0] - np.sum(a.components[1:] * b.components[1:])
        x_0, img_x = a.components[0], a.components[1:]
        y_0, img_y = b.components[0], b.components[1:]
        cross_part = self._octonion_cross_product(img_x, img_y)
        vector_part = x_0 * img_y + y_0 * img_x + cross_part
        return Octonion(np.concatenate(([real_part], vector_part)))
    
    def _octonion_cross_product(self, img_x: np.ndarray, img_y: np.ndarray) -> np.ndarray:
        """
        Compute the octonion imaginary part cross product.
        
        :param a: First octonion imaginary part.
        :param b: Second octonion imaginary part.
        :return: Resulting vector from the cross product.
        """
        fano_triples = [
            (0, 1, 2),
            (0, 3, 4),
            (0, 6, 5),
            (1, 3, 5),
            (1, 4, 6),
            (2, 3, 6),
            (2, 5, 4),
        ]
        cross_vector = np.zeros(7, dtype=img_x.dtype)
        for i, j, k in fano_triples:
            cross_vector[k] += img_x[i] * img_y[j] - img_x[j] * img_y[i]
            cross_vector[i] += img_x[j] * img_y[k] - img_x[k] * img_y[j]
            cross_vector[j] += img_x[k] * img_y[i] - img_x[i] * img_y[k] 
        return cross_vector
    
    def division(self, a: Octonion, b: Octonion) -> Octonion:
        """
        Divide two octonions.
        
        :param a: Numerator octonion.
        :param b: Denominator octonion.
        :return: Resulting octonion after division.
        """
        return self.multiply(a, self.inverse(b))