variables = {}

def errorBasic():
    return print("Error Variables, you must set name and a value!")

def error():
    return print("Error, set name and a value in your variable!")

def getError():
    return print("Give a name to get your variable")


def printAll():
    result = str(variables).replace("{", "")
    result2 = str(result).replace("}", "")
    result3 = str(result2).replace("'", "")
    return print(result3)


def getVariables(name):
    if name == "":
        getError()


def addVar(_name, _value):
    if _name == "":
        error()
    elif _value == "":
        error()
    else:
        variables.__setitem__(_name, _value) 