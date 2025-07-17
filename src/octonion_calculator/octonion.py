import numpy as np

class Octonion:
    def __init__(self,
                 e_0: float = 0, e_1: float = 0, e_2: float = 0, e_3: float = 0,
                 e_4: float = 0, e_5: float = 0, e_6: float = 0, e_7: float = 0):
        self.components: np.ndarray = np.array(
            [e_0, e_1, e_2, e_3, e_4, e_5, e_6, e_7],
            dtype=float
        )
    
    def __repr__(self):
        return f"Octonion({', '.join(f'{c:.2f}' for c in self.components)})"