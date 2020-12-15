## Error

def error():
    return print("Error, you must set a mode, two values")

## Function

def add(a, b):
    if a == 0 or b == 0:
        return print("Error, don't send '0'!")
    else:
        return print(a + b)

def remove(a, b):
    if a == 0 or b == 0:
        return print("Error, don't send '0'!")
    else:
        return print(a - b)

def div(a, b):
    if a == 0 or b == 0:
        return print("Error, don't send '0'!")
    else:
        return print(a / b)

def multi(a, b):
    if a == 0 or b == 0:
        return print("Error, don't send '0'!")
    else:
        return print(a * b)