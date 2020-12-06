import syntaxe
import PrInt
import var
import files

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
            else:
                var.errorBasic()

        if args[0] == "send":
            if len(args) == 1:
                var.sendError()
            elif len(args) == 2:
                if args[1] == "value":
                    var.printAll()
                else:
                    var.send(args[1])
            else:
                var.sendError()

        if args[0] == "set":
            if len(args) == 1:
                var.serError()
            else:
                name = args[1]
                value = args[1:1000000]
                var.setV(name, value)

        

        ## Files

        if args[0] == "files":
            if len(args) >= 2:
                if args[1] == "write":
                    f = args[2]
                    text = str(args[3:1000])
                    text = text.replace("[", "")
                    text = text.replace("]", "")
                    text = text.replace("'", "")
                    text = text.replace(",", "")
                    files.write(f, text)
                else:
                    files.errorWrite


                if args[1] == "read":
                    f = args[2]
                    files.reading(f)
                else:
                    files.errorRead()

                    
            else:
                files.error()