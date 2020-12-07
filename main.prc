variable MyVar = 1000
variable Bonjour = hello
send Bonjour
variable hallo = hallo
send hallo
setVar Bonjour hallo
send Bonjour
send hallo
mathPrint add 20 5
mathPrint remove 10 5
mathPrint multi 10 5
mathPrint div 100 10
math add MyVar 10
send MyVar
math remove MyVar 2
send MyVar
math multi MyVar 5
send MyVar
math div MyVar 2
send MyVar
files read r.txt
files write r.txt Hello Im a text!
files read r.txt