variables = {}

def errorBasic():
    return print("Error, you must set name and a value!")

def error():
    return print("Error, set name and a value in your variable!")

def getError():
    return print("Error, give a name to get your variable!")

def sendError():
    return print("Error, give the name!")

def setError():
    return print("Error, give the name and the new value!")


def printAll():
    result = str(variables).replace("{", "")
    result2 = str(result).replace("}", "")
    result3 = str(result2).replace("'", "")
    return print(result3)


def getVariables(name):
    if name == "":
        getError()
    else:
        return variables[name]


def addVar(_name, _value):
    if _name == "":
        error()
    elif _value == "":
        error()
    else:
        variables.__setitem__(_name, _value) 


def send(name):
    if name == "":
        sendError()
    else:
        return print(variables[name])

def setV(name, value):
    var = name
    newValue = value  
    variables[var] = newValue