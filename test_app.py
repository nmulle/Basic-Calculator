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
