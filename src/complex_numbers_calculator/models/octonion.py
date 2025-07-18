from .complex_number import ComplexNumber

class Octonion(ComplexNumber):
    """Class representing an octonion, a hypercomplex number with eight components."""
        
    def __repr__(self):
        """Return a string representation of the octonion."""
        return f"Octonion({', '.join(f'{c:.2f}' for c in self.components)})"