import sys
#sys.path.append("../src")
import pytest
from calculator.src.calculator import Calculator, NotANumber, NotAPositiveNumber

def test_add():
    """tests the Calculator add method"""
    calc = Calculator()
    assert calc.add(3) == 3

def test_subtract():
    """tests the Calculator subtract method"""
    calc = Calculator(5)
    assert calc.subtract(6) == -1

def test_multiply():
    """tests the Calculator multiply method"""
    calc = Calculator(2)
    assert calc.multiply(2) == 4

def test_divide():
    """tests the Calculator divide method"""
    calc = Calculator(9)
    assert calc.divide(3) == 3

def test_n_root():
    """tests the Calculator n_root method"""
    calc = Calculator(8)
    assert calc.n_root(3) == 2

def test_exponent():
    """tests the Calculator exponent method"""
    calc = Calculator(3)
    assert calc.exponent(3) == 27

def test_reset_memory():
    """tests the Calculator exponent method"""
    calc = Calculator(8)
    assert calc.reset_memory() == 0

def test_memory_value():
    """tests the Calculator exponent method"""
    calc = Calculator(8)
    assert calc.memory_value() == 8

def test_not_a_positive_number_error():
    calc = Calculator(-4)
    with pytest.raises(NotAPositiveNumber):
        result = calc.n_root(2)

def test_zero_division():
    calc = Calculator(4)
    with pytest.raises(ZeroDivisionError):
        result = calc.divide(0)

def test_input_validation():
    calc = Calculator(3)
    with pytest.raises(NotANumber):
        result = calc.add('three')

def test_input_validation_two():
    with pytest.raises(NotANumber):
        calc = Calculator('four')
