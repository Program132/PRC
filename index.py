mainPRC = "main.prc"

def re(mode, args):
    if mode == "pr":
        args = str(args).replace(",", "")
        args = str(args).replace("[", "")
        args = str(args).replace("]", "")
        args = str(args).replace("'", "")
        return args


class prc_errors:
    def __init__(self):
        self.basicError = "Error, give a name, =, and a value!"
        self.basicprintError = "Error, give arguments!"
        self.errorSetVar = "Error, give your variable and the new value!"
        self.basicerrorLenVar = "Error, give me your variable name!"
        self.basicErrorLen = "Error, give me a text!"
        self.basicerrorMath = "Error, give me two numbers/a variable and a number!"
        self.basicErrorInputVar = "Error, give me a variable who is definied and a text!"
        self.basicErrrorInputPrint = "Error, give me a text!"


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

    def errorMath(self):
        print(self.basicerrorMath)

    def inputVarError(self):
        print(self.basicErrorInputVar)

    def inputPrintError(self):
        print(self.basicErrrorInputPrint)



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



prc_Error = prc_errors()


class prc_main:
    def __init__(self):
        self.variables = {}

    # add var

    def addVar(self, name, value):
        if name and value: 
            self.variables[name] = value
        else:
            prc_Error.errorVar()
    
    # function to send a var

    def sendVar(self, name):
        print(self.variables[name])

    # Print text or print var

    def printing(self, arg):
        if arg[0] in self.variables.keys():
            print(self.variables[arg[0]])
        elif len(arg) >= 1:
            argument = re("pr", arg)
            print(argument)
        else:
            prc_Error.errorPrint()

    def setVar(self, arg, newvalue):
        if arg in self.variables.keys():
            self.variables[arg] = newvalue
        else:
            prc_Error.errorSet()

    



    ## math

    def mathPrint(self, nbr1, nbr2):
        try:
            print(int(nbr1) + int(nbr2))
        except:
            self.errorMath()

    def mathVar(self, mode, arg, nbr):
        if arg in self.variables.keys():
            if mode == "add":
                result = int(self.variables[arg]) + int(nbr)
                self.variables[arg] = result
            elif mode == "remove":
                result = int(self.variables[arg]) - int(nbr)
                self.variables[arg] = result
            elif mode == "multi":
                result = int(self.variables[arg]) * int(nbr)
                self.variables[arg] = result
            elif mode == "div":
                result = int(self.variables[arg]) / int(nbr)
                self.variables[arg] = result
            else:
                self.errorMath()
        else:
            self.errorMath()





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


    

            

    ## input

    def inputPrint(self, text):
        if len(text) >= 1:
            text = re("pr", text)
            print(input(text))
        else:
            self.inputPrintError()

    def inputVar(self, var, text):
        text = re("pr", text)
        variable = input(text)
        if var in self.variables.keys():
            self.variables[var] = variable
        else:
            self.inputVarError()




obj = prc_main()
obje = prc_prc()
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
                    else:
                        prc_Error.errorVar()
                else:
                    prc_Error.errorVar()


            if args[0] == "set":
                if len(args) == 3:
                    name = args[1]
                    value = args[2]
                    obj.setVar(name, value)
                else:
                    prc_Error.errorSetVar()


            
            ## prc

            if args[0] == "prc":
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
                else:
                    prc_Error.basicerrorLenVar()

                if len(args) >= 3:
                    obj.basicLen(args[1:])
                else:
                    prc_Error.basicErrorLen()
            

            ## math

            if args[0] == "mathPrint":
                if len(args) == 3:
                    obj.mathPrint(args[1], args[2])
                else:
                    prc_Error.errorMath()

            if args[0] == "math":
                if len(args) == 4:
                    mode = args[1]
                    var = args[2]
                    nbr = args[3]
                    obj.mathVar(mode, var, int(nbr))
                else:
                    prc_Error.errorMath()

            

            ## input

            if args[0] == "input":
                if len(args) >= 3 :
                    if args[1] == "print":
                        obj.inputPrint(args[2:])
                    else:
                        prc_Error.basicErrrorInputPrint()

                    if args[1] == "var":
                        obj.inputVar(args[2], args[3:])
                    else:
                        prc_Error.basicErrorInputVar()


            ## test

            if args[0] == "test":

                for arg in lines:
                    ar = arg.strip()
                    ar = ar.split()

                    if ar[0] == "cc":
                        print("cc est là!")

                    if ar[0] == "test2":
                        break