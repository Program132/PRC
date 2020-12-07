def error():
    return print("Error, check your code. If you use 'read' you must set file. If you use 'write', you must set file and a text.")

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