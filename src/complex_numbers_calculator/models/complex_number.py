from typing import Sequence

import numpy as np

class ComplexNumber():
    """
    Сlass for complex numbers
    """
    def __init__(self, components: Sequence[float]):
        self.components: np.ndarray = np.array(components,
            dtype=float
        )

    def __repr__(self):
        """Return a string representation of the complex number."""
        return f"ComplexNumber({', '.join(f'{c:.2f}' for c in self.components)})"

    @property
    def norm(self) -> float:
        """Calculate the norm of the complex number."""
        return np.linalg.norm(self.components)