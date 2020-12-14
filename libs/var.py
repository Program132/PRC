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
    try:
        resulte = variables[name]
        resulte1 = str(resulte).replace("[", '')
        resulte2 = str(resulte1).replace("]", '')
        resulte3 = str(resulte2).replace("'", '')
        resulte4 = str(resulte3).replace(",", '')
        return print(resulte4)
    except:
        return print("Error, your variable is not defined")
    

def setV(name, value):
    var = name
    newValue = value  
    variables[var] = newValue


# Math 

def matherror():
    return print("Error, you must set a mode, variable and a value.")

def mathAdd(name, value):
    try:
        result = int(variables[name]) + int(value)
        variables[name] = result
    except:
        print("Error, if it's string you can't use this. Change your code.")

def mathRem(name, value):
    try:
        result = int(variables[name]) - int(value)
        variables[name] = result
    except:
        print("Error, if it's string you can't use this. Change your code.")

def mathDiv(name, value):
    try:
        result = int(variables[name]) / int(value)
        variables[name] = result
    except:
        print("Error, if it's string you can't use this. Change your code.")

def mathMulti(name, value):
    try:
        result = int(variables[name]) * int(value)
        variables[name] = result
    except:
        print("Error, if it's string you can't use this. Change your code.")


## setVar

def setVarError():
    return print("Error, you must give 2 variables.")

def setVarEx(var1, var2):
    variables[var1] = variables[var2]


## Whil

def varSend(var, nbr):
    number = int(nbr)
    vari = variables[var]
    i = 0
    while i < number:
        print(vari)
        i = i + 1