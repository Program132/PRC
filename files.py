def error():
    return print("Error, you must set a file.")

def reading(_file):
    fichier = str(_file)
    f = open(fichier, "r")
    return print(f.readline())
    f.close()

def write(file, text):
    fichier = str(file)
    f = open(fichier, "w")
    return f.write(text)
    f.close()