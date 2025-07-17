import pytest
from octonion_calculator.octonion import Octonion


@pytest.fixture
def zero_octonion():
    """Fixture for a zero octonion."""
    sequence = [0.0] * 8
    return Octonion(sequence)
