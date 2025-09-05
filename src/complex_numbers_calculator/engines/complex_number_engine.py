from typing import TypeVar, Generic

import numpy as np

from ..models.complex_number import ComplexNumber

T = TypeVar('T')

class CompexNumberEngine(Generic[T]):
    """
    Abstract class for all engines
    """
    def __init__(self):
        """Initialize the engine"""
        pass

    def __repr__(self):
        """
        String representation of the complex numbers engine
        """
        return "ComplexNumber()"

    def add(self, a: T, b: T) -> T:
        """Add two complex numbers"""
        return type(a)(a.components + b.components)
    
    def subtract(self, a: T, b: T) -> T:
        """Subtract two complex numbers."""
        return type(a)(a.components - b.components)
    
    def conjugate(self, a: T) -> T:
        """Calculate the conjugate of the complex number."""
        return type(a)(np.concatenate([a.components[0:1], -a.components[1:]]))
    
    def inverse(self, a: T) -> T:
        """Calculate the inverse of the complex number."""
        norm_squared = a.norm ** 2
        if norm_squared == 0:
            raise ValueError("Cannot compute inverse of zero complex number.")
        conj_a = self.conjugate(a)
        return type(a)(conj_a.components / norm_squared)
    
    def multiply(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        """Multiply two complex numbers"""
        a_real, a_img = a.components
        b_real, b_img = b.components
        c_real = a_real * b_real - a_img * b_img
        c_img = a_img * b_real + a_real * b_img
        return ComplexNumber(np.array([c_real, c_img]))
    
    def division(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        """Devide two complex numbers"""
        conj_b = self.conjugate(b) 
        num = self.multiply(a, conj_b)
        denom = b.components[0]**2 + b.components[1]**2

        return ComplexNumber(num.components / denom)