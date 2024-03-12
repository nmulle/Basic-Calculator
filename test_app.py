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
