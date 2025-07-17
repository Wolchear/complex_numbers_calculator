import pytest
from octonion_calculator.octonion import Octonion


@pytest.fixture
def zero_octonion():
    """Fixture for a zero octonion."""
    return Octonion(0, 0, 0, 0, 0, 0, 0, 0)