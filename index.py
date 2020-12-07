import PrInt
import var
import files
import mathPrint

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

        if args[0] == "setVar":
            if len(args) == 3:
                variable1 = args[1]
                variable2 = args[2]
                var.setVarEx(variable1, variable2)
            else:
                var.setVarError()

        if args[0] == "math":
            if len(args) == 4:
                mode = args[1]
                v = args[2]
                value = args[3]
                if mode == "add":
                    var.mathAdd(v, value)
                elif mode == "remove":
                    var.mathRem(v, value)
                elif mode == "div":
                    var.mathDiv(v, value)
                elif mode == "multi":
                    var.mathMulti(v, value)
            else:
                var.matherror()

        
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


                if args[1] == "read":
                    f = args[2]
                    files.reading(f)

            else:
                files.error()



        ## MathPrint

        if args[0] == "mathPrint":
            if len(args) >= 3:
                a = int(args[2])
                b = int(args[3])
                if args[1] == "add":
                    mathPrint.add(a, b)
                elif args[1] == "remove":
                    mathPrint.remove(a, b)
                elif args[1] == "div":
                    mathPrint.div(a, b)
                elif args[1] == "multi":
                    mathPrint.multi(a, b)
            else:
                mathPrint.error()