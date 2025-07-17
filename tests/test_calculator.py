def test_addition(octonion_calculator, zero_octonion, one_octonion):
    """Test the addition of a zero octonion with another octonion."""
    sum_result = octonion_calculator.add(zero_octonion, one_octonion)
    assert repr(sum_result) == "Octonion(1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)"

def test_subtraction(octonion_calculator, zero_octonion, one_octonion):
    """Test the subtraction of a zero octonion from another octonion."""
    diff_result = octonion_calculator.subtract(one_octonion, zero_octonion)
    assert repr(diff_result) == repr(one_octonion)

def test_calculator_repr(octonion_calculator):
    """Test the engine representation of the calculator."""
    assert repr(octonion_calculator) == "Calculator using engine: OctonionEngine()"
    
def test_multply(octonion_calculator, inc_octonion):
    """Test the multiplication of a zero octonion with another octonion."""
    product_result = octonion_calculator.multiply(inc_octonion, inc_octonion)
    assert repr(product_result) == "Octonion(-202.00, 4.00, 6.00, 8.00, 10.00, 12.00, 14.00, 16.00)"