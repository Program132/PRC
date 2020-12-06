def error():
    return print("Error, you must set a file.")

def reading(_file):
    fichier = str(_file)
    f = open(fichier, "r")
    return print(f.readline())

def write(file, text):
    return print("Writing...")