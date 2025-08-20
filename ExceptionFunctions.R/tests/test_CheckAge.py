from functions.exceptionFunctions import checkAge
import pytest

@pytest.mark.parametrize("Age, result", [
    (2, True),
    (4, True),
    (24, True),
    (3, True),
    (0, True),
    (-1, "Age cannot be negative")
])

def test_CheckAge(Age :int, result):
    try:
        assert checkAge(Age) == result
    except Exception:
        assert Age < 0 == "Age cannot be negative"