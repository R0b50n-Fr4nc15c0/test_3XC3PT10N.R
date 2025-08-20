from functions.exceptionFunctions import validateUsername
import pytest

@pytest.mark.parametrize("username, result", [
    ("usuario123", "usuario123"),
    ("usuario_321", "Username must contain only letters and numbers")
])

def test_validateUsername(username, result):
    try:
        assert validateUsername(username) == result
    except Exception:
        assert not username.isalnum() == "Username must contain only letters and numbers"