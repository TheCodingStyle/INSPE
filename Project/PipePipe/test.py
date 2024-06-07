e = [["output", '"', "Salut", "Je", "M'appelle", "Malik", '"']]
r = 0
for i in e:
    print(len(i) - 1)
    if i[r] == "output":
        r += 1
        if i.index('"') == r:
            r += 1
            while i[r] != '"':
                print(i[r], end=" ")
                r += 1
            print("\n")
            
    