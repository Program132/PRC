variables = {}

variables.type= {
    "string",
    "int",
    "boolean"
}

def error():
    return print("Error, set name, type and value in your variable!")

def addVar(_name, _type, _value):
    if _name == "":
        error()
    else:
        if _type == "":
            error()
        else:
            if _value == "":
                error()
            else:
                ...

def printAll():
    print(variables)