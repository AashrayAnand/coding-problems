def permutations(s):
    res = []
    intermediate = []
    for i, letter in enumerate(s):
        intermediate.append((letter, s[0:i] + s[i+1:]))
    
    while len(intermediate) > 0:
        # get head of list
        shortstr = intermediate.pop(0)
        if len(shortstr[1]) == 0:
            res.append(shortstr[0])
        else:
            for i, letter in enumerate(shortstr[1]):
                intermediate.append((shortstr[0] + letter, shortstr[1][0: i] + shortstr[1][i + 1:]))
    
    print(res)
    print(len(res))

permutations("ABCDEF")
