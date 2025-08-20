from functions.exceptionFunctions import withdraw
import pytest

@pytest.mark.parametrize("balance, amount, result", [
    (200, 150, 50),
    (500, 480, 20),
    (200, 250, "Insufficient funds")
])

def test_withdraw(balance,amount, result):
    try:
        assert withdraw(balance, amount) == result
    except Exception:
        assert amount > balance == "Insufficient funds"