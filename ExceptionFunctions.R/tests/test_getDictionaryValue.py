from functions.exceptionFunctions import getDictionaryValue
import pytest

@pytest.mark.parametrize("data, key, result", [
    ("nome", "João", "João"),
    ("idade", "João", None),
])

def test_getDictionaryValue(data, key, result):
    try:
        assert getDictionaryValue(data, key) == result
    except Exception:
        assert key not in data == f"Key '{key}' not found in dictionary"