from functions.exceptionFunctions import factorial
import pytest

@pytest.mark.parametrize("n, result", [
    (5, 120),
    (0, 1),
    (1, 1),
    (-1, "Factorial is not defined for negative numbers")
])

def test_factorial(n, result):
    try:
        assert factorial(n) == result
    except Exception:
        assert n < 0 == "Factorial is not defined for negative numbers"