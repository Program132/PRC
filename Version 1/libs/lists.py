allLists = {}

## Errors

def error():
    return print("Error, you must give a name and arguments!")

def errorSend():
    return print("Error, you must give a name!")

def errorMode():
    return print("Error, you must give a mode!")


## Functions

def addList(name, value):
    allLists[name] = value
    

def sendList(name):
    try:
        return print(allLists[name])
    except:
        return print("Error, your list is not definied.")