from typing import Sequence

import numpy as np

class Octonion:
    """Class representing an octonion, a hypercomplex number with eight components."""
    def __init__(self, components: Sequence[float]):
        self.components: np.ndarray = np.array(components,
            dtype=float
        )

    def __repr__(self):
        """Return a string representation of the octonion."""
        return f"Octonion({', '.join(f'{c:.2f}' for c in self.components)})"

    @property
    def norm(self) -> float:
        """Calculate the norm of the octonion."""
        return np.linalg.norm(self.components)
    