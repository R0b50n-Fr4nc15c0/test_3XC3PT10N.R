from functions.exceptionFunctions import setTemperature
import pytest

@pytest.mark.parametrize("temp, result", [
    (-260, -260),
    (-236, -236),
    (-299, "Temperature cannot be below absolute zero")
])

def test_setTemperature(temp, result):
    try:
        assert setTemperature(temp) == result
    except Exception:
        assert temp < -273. == "Temperature cannot be below absolute zero"