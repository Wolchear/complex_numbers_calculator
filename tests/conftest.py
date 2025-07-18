import pytest
from complex_numbers_calculator.models import Octonion
from complex_numbers_calculator import Calculator
from complex_numbers_calculator.models import ComplexNumber

@pytest.fixture
def zero_octonion():
    """Fixture for a zero octonion."""
    sequence = [0.0] * 8
    return Octonion(sequence)

@pytest.fixture
def one_octonion():
    """Fixture for a one octonion."""
    sequence = [1.0] + [0.0] * 7
    return Octonion(sequence)

@pytest.fixture
def inc_octonion():
    """Fixture for an increment octonion."""
    sequence = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    return Octonion(sequence)

@pytest.fixture
def octonion_calculator():
    """Fixture for the octonion calculator."""
    return Calculator(engine_name='octonion')

@pytest.fixture
def complex_number_calculator():
    """Fixture for the complex number calculator."""
    return Calculator(engine_name='complex_number')

@pytest.fixture
def norm_octonion():
    """Fixture for a normalized octonion."""
    sequence = [1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0]
    return Octonion(sequence)

@pytest.fixture
def complex_number():
    """Fixture for a complex number."""
    sequence = [1.0, -3.0]
    return ComplexNumber(sequence)

@pytest.fixture
def complex_number_second():
    """Fixture for a complex number."""
    sequence = [2.0, 5.0]
    return ComplexNumber(sequence)