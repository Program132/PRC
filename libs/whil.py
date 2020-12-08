def error():
    return print("Error, you must set : a mode, a checkmode(>, <),2 number (when we start and when it's finish) and to finish print or others(if it's your mode.).")

def checkError():
    return print("Error, your mode is not valid : > and <!")

## Print

def printWhilMoinsGrand(nbr1, nbr2, text):
    i = int(nbr1)
    b = int(nbr2)
    txt = str(text).replace("[", "")
    txt = str(txt).replace("]", "")
    txt = str(txt).replace("'", "")
    while i < b:
        i = i + 1
        print(txt)

def printWhilgrandMoins(nbr1, nbr2, text):
    i = int(nbr1)
    b = int(nbr2)
    txt = str(text).replace("[", "")
    txt = str(txt).replace("]", "")
    txt = str(txt).replace("'", "")
    while i > b:
        i = i - 1
        print(txt)