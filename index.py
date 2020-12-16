mainPRC = "main.prc"

def replace(mode, args):
    if mode == "pr":
        args = str(args).replace(",", "")
        args = str(args).replace("[", "")
        args = str(args).replace("]", "")
        args = str(args).replace("'", "")
        return args

class prc_prc:
    def __init__(self):
        self.error = "Error, give a argument/valid argument!"

    def erro(self):
        print(self.error)

    def about(self):
        print("PRC is a programing language create by Program. PRC will evolve and be improved over time.")

    def discord(self):
        print("Join the server discord. https://discord.com/invite/e44jCnpTqA")

    def website(self):
        print("The website of the project. https://program132.github.io/PRC/index.html")

    def doc(self):
        print("Documentation. https://program132.github.io/PRC/doc.html")


class prc_variablesPrint:
    def __init__(self):
        self.basicError = "Error, give a name, =, and a value!"
        self.basicprintError = "Error, give arguments!"
        self.errorSetVar = "Error, give your variable and the new value!"
        self.basicerrorLenVar = "Error, give me your variable name!"
        self.basicErrorLen = "Error, give me a text!"
        self.variables = {}

    ## Errors

    def errorVar(self):
        print(self.basicError)

    def errorPrint(self):
        print(self.basicprintError)

    def errorSet(self):
        print(self.errorSetVar)

    def errorLenVar(self):
        print(self.basicerrorLenVar)

    def errorLen(self):
        print(self.basicErrorLen)



    #### Var

    def addVar(self, name, value):
        if name and value: 
            self.variables[name] = value
        else:
            self.errorVar()

    def sendVar(self, name):
        print(self.variables[name])

    # Print text or print var

    def printing(self, arg):
        if len(arg) == 1 and arg[0] in self.variables.keys():
            print(self.variables[arg[0]])
        elif len(arg) > 1:
            argument = replace("pr", arg)
            print(argument)
        else:
            self.errorPrint()

    def setVar(self, arg, newvalue):
        if arg in self.variables.keys():
            self.variables[arg] = newvalue
        else:
            self.errorSet()




    #### len

    # text
    def basicLen(self, text):
        if len(text) >= 1:
            print(len(text))
        else:
            self.errorLen()

    # value of an variable

    def lenVar(self, name):
        if name in self.variables.keys():
            print("1")
        elif name not in self.variables.keys():
            self.basicLen(name)
        else:
            self.errorLenVar()


obj = prc_variablesPrint()
with open(mainPRC, "r+")as f:
    lines = f.readlines()
    
    for lin in lines:
        line = lin.strip()
        args = line.split()

        if len(args) >= 0:

            ## Print

            if args[0] == "print":
                obj.printing(args[1:])



            ## Variables

            if args[0] == "variable":
                if len(args) == 4:
                    name = args[1]
                    equal = args[2]
                    value = args[3]
                    if equal == "=":
                        obj.addVar(name, value)


            if args[0] == "set":
                if len(args) == 3:
                    name = args[1]
                    value = args[2]
                    obj.setVar(name, value)


            
            ## prc

            if args[0] == "prc":
                obje = prc_prc()
                if len(args) == 2:
                    argu  = args[1]
                    if argu == "about":
                        obje.about()
                    elif argu == "discord":
                        obje.discord()
                    elif argu == "website" or argu == "web" or argu == "site":
                        obje.website()
                    elif argu == "doc" or argu == "documentation":
                        obje.doc()
                    else:
                        obje.erro()
                else:
                    obje.erro()



            ## len

            if args[0] == "len":
                if len(args) == 2:
                    obj.lenVar(args[1])
                elif len(args) >= 3:
                    obj.basicLen(args[1:])