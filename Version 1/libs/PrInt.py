def Basic(arg):
    try:
        return print(arg)
    except:
        return Error()

def Error():
    return print("Error Print! You must set a argument in your print.")

def DontFound():
    return print("Print don't found...")