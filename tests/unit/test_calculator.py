import pytest

class TestOctonionCalculator:
    """Class for the octonion calculator testing."""
    def test_calculator_repr(self, octonion_calculator):
        """Test the engine representation of the calculator."""
        assert repr(octonion_calculator) == "Calculator using engine: OctonionEngine()"
    
    @pytest.mark.parametrize(
        "seq_1, seq_2, ref_result",
        [
            pytest.param([0.0] * 8,
                         [1.0] + [0.0] * 7,
                         "Octonion(1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)",
                         id='zero+one'),
            pytest.param([0.0] * 8,
                         [0.0] * 8,
                         "Octonion(0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)",
                         id='zero+zero'),
            pytest.param([1, 1, 2, 3, 1, -2.5, 1.2, 3],
                         [0,-0.5, 2,-1, -1.5, 3.2, 0.7, -0.5],
                         "Octonion(1.00, 0.50, 4.00, 2.00, -0.50, 0.70, 1.90, 2.50)",
                         id='rand+rand'),
        ]
    )
    def test_addition(self, octonion_calculator, make_octonion, seq_1, seq_2, ref_result):
        """Test the addition of octonion with another octonion."""
        octonion_1 = make_octonion(seq_1)
        octonion_2 = make_octonion(seq_2)
        sum_result = octonion_calculator.add(octonion_1, octonion_2)
        assert repr(sum_result) == ref_result
    
    @pytest.mark.parametrize(
        "seq_1, seq_2, ref_result",
        [
            pytest.param([0.0] * 8,
                         [1.0] + [0.0] * 7,
                         "Octonion(-1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)",
                         id='zero-one'),
            pytest.param([1, 1, 2, 3, 1, -2.5, 1.2, 3],
                         [0,-0.5, 2,-1, -1.5, 3.2, 0.7, -0.5],
                         "Octonion(1.00, 1.50, 0.00, 4.00, 2.50, -5.70, 0.50, 3.50)",
                         id='rand-rand'),
        ]
    )
    def test_subtraction(self, octonion_calculator, make_octonion, seq_1, seq_2, ref_result):
        """Test the subtraction of octonion from another octonion."""
        octonion_1 = make_octonion(seq_1)
        octonion_2 = make_octonion(seq_2)
        diff_result = octonion_calculator.subtract(octonion_1, octonion_2)
        assert repr(diff_result) == ref_result
    
    @pytest.mark.parametrize(
        "seq_1, seq_2, ref_result",
        [
            pytest.param([0.0] * 8,
                         [1.0] + [0.0] * 7,
                         "Octonion(0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)",
                         id='zero*one'),
            pytest.param([1, 1, 2, 3, 1, -2.5, 1.2, 3],
                         [0,-0.5, 2, -1, -1.5, 3.2, 0.7, -0.5],
                         "Octonion(9.66, -6.35, -4.35, 11.59, -3.95, 12.50, -10.40, 6.10)",
                         id='rand*rand'),
        ]
    )
    def test_multply(self, octonion_calculator, make_octonion, seq_1, seq_2, ref_result):
        """Test the multiplication of octonion with another octonion."""
        octonion_1 = make_octonion(seq_1)
        octonion_2 = make_octonion(seq_2)
        product_result = octonion_calculator.multiply(octonion_1, octonion_2)
        assert repr(product_result) == ref_result
    
    @pytest.mark.parametrize(
        "seq_1, seq_2, ref_result",
        [
            pytest.param([0.0] * 8,
                         [1.0] + [0.0] * 7,
                         "Octonion(0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)",
                         id='zero/one'),
            pytest.param([1, 1, 2, 3, 1, -2.5, 1.2, 3],
                         [0,-0.5, 2, -1, -1.5, 3.2, 0.7, -0.5],
                         "Octonion(-0.52, 0.34, 0.24, -0.63, 0.21, -0.68, 0.56, -0.33)",
                         id='rand/rand'),
        ]
    )    
    def test_division(self, octonion_calculator, make_octonion, seq_1, seq_2, ref_result):
        """Test the division of octonion by another octonion."""
        octonion_1 = make_octonion(seq_1)
        octonion_2 = make_octonion(seq_2)
        division_result = octonion_calculator.division(octonion_1, octonion_2)
        assert repr(division_result) == ref_result
        
    def test_division_by_zero(self, octonion_calculator, make_octonion):
        """Test division by a zero octonion raises ValueError."""
        with pytest.raises(ZeroDivisionError) as excinfo:
            octonion_1 = make_octonion([1.0] + [0.0] * 7)
            octonion_2 = make_octonion([0.0] * 8)
            octonion_calculator.division(octonion_1, octonion_2)
        assert 'Could not compute division by zero' in str(excinfo.value)
        
class TestComplexNumbersCalculator:
    """Class for the Complex Numbers calculator testing."""
    @pytest.mark.parametrize(
        "seq_1, ref_result",
        [
            pytest.param([3.00, 1.00],
                         "ComplexNumber(3.00, -1.00)",
                         id='complex_conj'),
            pytest.param([0.00, 0.00],
                         "ComplexNumber(0.00, -0.00)",
                         id='zero_conj'),
        ]
    )    
    def test_conjugate(self, complex_number_calculator, make_complex, seq_1, ref_result):
        """Test the conjugate of a complex number."""
        complex_number = make_complex(seq_1)
        conjugate_result = complex_number_calculator.conjugate(complex_number)
        assert repr(conjugate_result) == ref_result
        
    @pytest.mark.parametrize(
        "seq_1, ref_result",
        [
            pytest.param([3.00, 1.00],
                         "ComplexNumber(0.30, -0.10)",
                         id='complex_conj'),
        ]
    )     
    def test_inverse(self, complex_number_calculator, make_complex, seq_1, ref_result):
        """Test the inverse of a complex number."""
        complex_number = make_complex(seq_1)
        inverse_result = complex_number_calculator.inverse(complex_number)
        assert repr(inverse_result) == ref_result
    
    def test_inverse_by_zero(self, complex_number_calculator, make_complex):
        """Test inverse of a zero complex number raises ValueError."""
        with pytest.raises(ValueError) as excinfo:
            complex_number = make_complex([0.0, 0.0])
            complex_number_calculator.inverse(complex_number)
        assert 'Cannot compute inverse of zero complex number.' in str(excinfo.value)
    
    @pytest.mark.parametrize(
        "seq_1, seq_2, ref_result",
        [
            pytest.param([1.0, -3.0],
                         [2.0, 5.0],
                         "ComplexNumber(17.00, -1.00)",
                         id='complex*complex'),
            pytest.param([1.00, 1.00],
                         [0.00, 0.00],
                         "ComplexNumber(0.00, 0.00)",
                         id='complex*zero'),
        ]
    )    
    def test_complex_multiply(self, complex_number_calculator,
                              make_complex, seq_1, seq_2, ref_result):
        """Test the multiplication of two complex numbers."""
        complex_number_1 = make_complex(seq_1)
        complex_number_2 = make_complex(seq_2)
        product_result = complex_number_calculator.multiply(complex_number_1, complex_number_2)
        assert repr(product_result) == ref_result