from functions.exceptionFunctions import validateEmail
import pytest

@pytest.mark.parametrize("email, result", [
    ("RobinhoFrancisco@gmail.com", True),
    ("robsonsantosgmail.com", None)
])

def test_validateEmail(email, result):
    try:
        assert validateEmail(email) == result
    except Exception:
        assert "@" not in email or "." not in email == "Invalid email format"