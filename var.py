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
        resulte = variables[name]
        resulte1 = str(resulte).replace("[", '')
        resulte2 = str(resulte1).replace("]", '')
        resulte3 = str(resulte2).replace("'", '')
        resulte4 = str(resulte3).replace(",", '')
        return print(resulte4)

def setV(name, value):
    var = name
    newValue = value  
    variables[var] = newValue