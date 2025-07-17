def test_addition(octonion_calculator, zero_octonion, one_octonion):
    """Test the addition of a zero octonion with another octonion."""
    sum_result = octonion_calculator.add(zero_octonion, one_octonion)
    assert repr(sum_result) == "Octonion(1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)"

def test_calculator_repr(octonion_calculator):
    """Test the engine representation of the calculator."""
    assert repr(octonion_calculator) == "Calculator using engine: OctonionEngine()"
