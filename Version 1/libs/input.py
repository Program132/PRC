## Errors

def error():
    return print("Error, give a value.")

def errorNtFound():
    return print("Error, mode not found.")

## Functions

def inputBasic(args):
    arg = str(args).replace("[", "")
    arg = str(arg).replace("]", "")
    arg = str(arg).replace(",", "")
    arg = str(arg).replace("'", "")
    arg = str(arg).replace('"', "")
    result = input(arg)
    return result

def inputPrint(args):
    arg = str(args).replace("[", "")
    arg = str(arg).replace("]", "")
    arg = str(arg).replace(",", "")
    arg = str(arg).replace("'", "")
    arg = str(arg).replace('"', "")
    result = input(arg)
    return print("Answer : " + result)