import syntaxe
import PrInt
import var

with open("main.prc", "r+") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        args = line.split()

        ## Print


        if args[0] == "print":
            if len(args) == 1:
                PrInt.Error()
            elif len(args) >= 2:
                value, *b = args
                b = " ".join(b)
                PrInt.Basic(b)
            else: 
                PrInt.DontFound()



        ## Variables

        if args[0] == "variable":
            if len(args) == 1:
                var.errorBasic()
            elif len(args) == 2:
                var.errorBasic()
            elif len(args) == 3:
                var.errorBasic()
            elif len(args) == 4:
                if args[2] == "=":
                    var.addVar(args[1], args[3])
                    #var.printAll()
            else:
                var.errorBasic()