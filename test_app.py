from app import BasicCalculator
import pytest


# Get a fresh calculator instance
@pytest.fixture
def calculator():
    return BasicCalculator()

def test_add(calculator):
    assert calculator.add(0, 0) == 0
    assert calculator.add(-5, -3) == -8
    assert calculator.add(7, 2) == 9
    assert calculator.add(3, -6) == -3

def test_subtract(calculator):
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-5, -3) == -2
    assert calculator.subtract(7, 2) == 5
    assert calculator.subtract(3, -6) == 9

def test_multiply(calculator):
    assert calculator.multiply(0, 0) == 0
    assert calculator.multiply(-4, -7) == 28
    assert calculator.multiply(3, 12) == 36
    assert calculator.multiply(5, -6) == -30

def test_divide(calculator):
    assert calculator.divide(0, 3) == 0
    assert calculator.divide(-4, 2) == -2
    assert calculator.divide(12, 3) == 4
    assert calculator.divide(10, -2) == -5

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(3, 0)
