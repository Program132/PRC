import syntaxe
import PrInt

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

        else:
            syntaxe.error()