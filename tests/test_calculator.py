import pytest

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
    
def test_multply(octonion_calculator, norm_octonion):
    """Test the multiplication of a zero octonion with another octonion."""
    product_result = octonion_calculator.multiply(norm_octonion, norm_octonion)
    assert repr(product_result) == "Octonion(-58.00, 4.00, 6.00, 8.00, 8.00, 6.00, 4.00, 2.00)"
    
def test_division(octonion_calculator, norm_octonion, one_octonion):
    """Test the division of a zero octonion by another octonion."""
    division_result = octonion_calculator.division(norm_octonion, one_octonion)
    assert repr(division_result) == repr(norm_octonion)
    
def test_division_by_zero(octonion_calculator, norm_octonion, zero_octonion):
    """Test division by a zero octonion raises ValueError."""
    with pytest.raises(ValueError) as excinfo:
        octonion_calculator.division(norm_octonion, zero_octonion)
    assert "Cannot compute inverse of zero octonion." in str(excinfo.value)