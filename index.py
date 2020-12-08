import libs.prc
import libs.PrInt
import libs.var
import libs.files
import libs.mathPrint
import libs.whil

with open("main.prc", "r+") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        args = line.split()

        ## PRC
        try:
            if args[0] == "prc":
                if len(args) == 2:
                    try:
                        if args[1] == "doc" or args[1] == "documentation":
                            libs.prc.doc()
                        elif args[1] == "about":
                            libs.prc.about()
                        elif args[1] == "discord":
                            libs.prc.discord()
                        elif args[1] == "website" or args[1] == "site" or args[1] == "web":
                            libs.prc.website()
                        else:
                            libs.prc.error()
                    except:
                        libs.prc.error()
                else:
                    libs.prc.error()

            ## Print


            if args[0] == "print":
                if len(args) == 1:
                    libs.PrInt.Error()
                elif len(args) >= 2:
                    value, *b = args
                    b = " ".join(b)
                    libs.PrInt.Basic(b)
                else: 
                    libs.PrInt.DontFound()



            ## Variables

            if args[0] == "variable":
                if len(args) == 1:
                    libs.var.errorBasic()
                elif len(args) == 2:
                    libs.var.errorBasic()
                elif len(args) == 3:
                    libs.var.errorBasic()
                elif len(args) == 4:
                    if args[2] == "=":
                        libs.var.addVar(args[1], args[3])
                else:
                    libs.var.errorBasic()

            if args[0] == "send":
                if len(args) == 1:
                    libs.var.sendError()
                elif len(args) == 2:
                    if args[1] == "value":
                        libs.var.printAll()
                    else:
                        libs.var.send(args[1])
                else:
                    libs.var.sendError()

            if args[0] == "set":
                if len(args) == 1:
                    libs.var.serError()
                else:
                    name = args[1]
                    value = args[1:1000000]
                    libs.var.setV(name, value)

            if args[0] == "setVar":
                if len(args) == 3:
                    variable1 = args[1]
                    variable2 = args[2]
                    libs.var.setVarEx(variable1, variable2)
                else:
                    libs.var.setVarError()

            if args[0] == "math":
                if len(args) == 4:
                    mode = args[1]
                    v = args[2]
                    value = args[3]
                    if mode == "add":
                        libs.var.mathAdd(v, value)
                    elif mode == "remove":
                        libs.var.mathRem(v, value)
                    elif mode == "div":
                        libs.var.mathDiv(v, value)
                    elif mode == "multi":
                        libs.var.mathMulti(v, value)
                else:
                    libs.var.matherror()

            
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
                        libs.files.write(f, text)


                    if args[1] == "read":
                        f = args[2]
                        libs.files.reading(f)

                else:
                    libs.files.error()



            ## MathPrint

            if args[0] == "mathPrint":
                if len(args) >= 3:
                    a = int(args[2])
                    b = int(args[3])
                    if args[1] == "add":
                        libs.mathPrint.add(a, b)
                    elif args[1] == "remove":
                        libs.mathPrint.remove(a, b)
                    elif args[1] == "div":
                        libs.mathPrint.div(a, b)
                    elif args[1] == "multi":
                        libs.mathPrint.multi(a, b)
                else:
                    libs.mathPrint.error()


            ## Check
            if args[0] == "whil":
                try:
                    if args[1] == "print":
                        if args[2] == "<": #check mode
                            text = args[5:1000000]
                            nbr1 = args[3]
                            nbr2 = args[4]
                            libs.whil.printWhilMoinsGrand(nbr1, nbr2, text)
                        elif args[2] == ">": #check mode
                            text = args[5:1000000]
                            nbr1 = args[3]
                            nbr2 = args[4]
                            libs.whil.printWhilgrandMoins(nbr1, nbr2, text)
                        else:
                            libs.whil.checkError()
                    elif args[1] == "varSend":
                        variable = args[2]
                        nbrX = args[3]
                        libs.var.varSend(variable, nbrX)
                except:
                    libs.whil.error()
        except:
            print("Check if you file has content")