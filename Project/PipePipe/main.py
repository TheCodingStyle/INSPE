with open("file.av", "r") as file:
    liste = []
    
    for line in file:
        liste.append(
            line.split()
        )  
lexer = {}
variables_type = ["Ivar", "Fvar", "Svar", "Bvar"]

valide = 0

for line in liste:
    if line[valide] in variables_type: 
        valide += 1 #type checked
        if bool(line[valide]) == True: #name checked
            lexer[line[valide]] = None
            valide += 1
            if line[valide] == "?": 
                variable_value = input()
                lexer[line[valide - 1]] = variable_value
                valide = 0
            if bool(line[valide]) == True and line[valide - 2] == "Ivar":
                lexer[line[valide - 1]] = int(line[valide])
                valide = 0
            elif bool(line[valide]) == True and line[valide - 2] == "Fvar":
                lexer[line[valide - 1]] = float(line[valide])
                valide = 0
            elif (bool(line[valide]) == True and line[valide - 1] == "Bvar"):
                if line[valide] == "is" or line[valide] == "is_not":
                    if "is":
                        lexer[line[valide - 1]] = True
                    else :
                        lexer[line[valide - 1]] = line[valide]
                        
    if line[valide] == "output":
        valide += 1
        
        if line[valide] in lexer:
            print(lexer[line[valide]])
            valide = 0
            
        elif str(line[valide]).isdigit():
            if line[valide + 1] not in ["+", "-", "*", "/"]:
                print(line[valide])
            else:
                stack = []
                for i in range(1, len(line)):
                    if str(line[i]).isdigit():
                        stack.append(int(line[i]))
                    else:
                        stack.append(line[i])
                expr_str = ''.join(map(str, stack))
                result = eval(expr_str)
                print(result)
                valide = 0
                

        elif line.index('"') == valide:
                valide += 1
                while line[valide] != '"':
                    print(line[valide], end=" ")
                    valide += 1
                valide = 0
                print() 
        
        