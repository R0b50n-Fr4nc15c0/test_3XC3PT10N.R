from functions.exceptionFunctions import squareRoot
import pytest

@pytest.mark.parametrize("x, result", [
    (121, 11),
    (144, 12),
    (9, 3),
    (-1, "Cannot calculate square root of negative number")
])

def test_squareRoot(x, result):
    try:
        assert squareRoot(x) == result
    except Exception:
        assert x < 0 == "Cannot calculate square root of negative number"