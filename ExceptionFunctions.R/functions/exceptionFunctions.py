def checkAge(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True


def validateEmail(email: str):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    return True


def withdraw(balance: float, amount: float):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


def squareRoot(x: float):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return x ** 0.5
    

def validatePassword(password: str):
    if len(password) < 6:
        raise ValueError("Password too short")
    return True


def findElement(elements: list, value):
    if value not in elements:
        raise LookupError("Element not found in list")
    return value


def setTemperature(temp: float):
    if temp < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")
    return temp


def factorial(n: int):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def getDictionaryValue(data: dict, key: str):
    if key not in data:
        raise KeyError(f"Key '{key}' not found in dictionary")
    return data[key]


def validateUsername(username: str):
    if not username.isalnum():
        raise ValueError("Username must contain only letters and numbers")
    return username
