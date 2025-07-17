import pytest

from octonion_calculator.engines import get_engine

def test_engine_factory():
    """Test the engine factory creation."""
    engine = get_engine("octonion")
    assert repr(engine) == "OctonionEngine()"
    
def test_engine_factory_invalid():
    """ValueError should be raised for an invalid engine."""
    with pytest.raises(ValueError) as excinfo:
        get_engine("nonexistent_engine")
    assert "Engine 'nonexistent_engine' is not supported." in str(excinfo.value)