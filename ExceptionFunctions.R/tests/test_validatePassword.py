from functions.exceptionFunctions import validatePassword
import pytest

@pytest.mark.parametrize("password, result", [
    ("g43cs8", True),
    ("44rr53", True),
    ("gt566", "Password too short")
])

def test_validatePassword(password, result):
    try:
        assert validatePassword(password) == result
    except Exception:
        assert len(password) < 6 == "Password too short"