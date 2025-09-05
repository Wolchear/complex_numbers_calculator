import pytest
from complex_numbers_calculator.models import Octonion
from complex_numbers_calculator import Calculator
from complex_numbers_calculator.models import ComplexNumber

@pytest.fixture(scope='session')
def make_octonion():
    """Fixture for an octonion facroty."""
    def _make_octonion(seq):
        return Octonion(seq)
    
    return _make_octonion

@pytest.fixture(scope='session')
def make_complex():
    """Fixture for an complex numbers facroty."""
    def _make_complex(seq):
        return ComplexNumber(seq)
    
    return _make_complex

@pytest.fixture
def zero_octonion():
    """Fixture for a zero octonion."""
    sequence = [0.0] * 8
    return Octonion(sequence)

@pytest.fixture(scope='session')
def octonion_calculator():
    """Fixture for the octonion calculator."""
    return Calculator(engine_name='octonion')

@pytest.fixture(scope='session')
def complex_number_calculator():
    """Fixture for the complex number calculator."""
    return Calculator(engine_name='complex_number')
