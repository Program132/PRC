import libs.var

## Errors

def error():
    return print("Error, please check your code with this function.")

def errorArg(arg):
    if arg == "basic":
        return print("Error, you must give a valid mode, ( and ) and arg, to finish, add =>!")
    elif arg == '(' or arg == ')':
        return print("Error, you must set '(' to open and ')' to close.")
    elif arg == "=>":
        return print("Error, to finish your 'check', you must add =>!")
    elif arg == "mode":
        return print("Error, give me a valid mode!")



## Function => var.py
