from functions.exceptionFunctions import findElement
import pytest

@pytest.mark.parametrize("elements, value, result", [
    ((1,2,3,4,5,6,7,8,9), 4, 4),
    (("Rogerio", "Pamela", "Marzio", "Miguel"), "Pamela", "Pamela"),
    ((1,2,3,4,5,6,7,8), 9, "Element not found in list")
])

def test_findElement(elements, value, result):
    try:
        assert findElement(elements, value) == result
    except Exception:
        assert value not in elements == "Element not found in list"