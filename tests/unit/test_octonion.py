def test_repr_zero(zero_octonion):
    """Test the string representation of a zero octonion."""
    assert repr(zero_octonion) == "Octonion(0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)"
