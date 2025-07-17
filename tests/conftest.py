import pytest
from octonion_calculator.models.octonion import Octonion
from octonion_calculator import Calculator

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
def octonion_calculator():
    """Fixture for the octonion calculator."""
    return Calculator(engine_name='octonion')
