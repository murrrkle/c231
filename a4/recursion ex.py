def flatten(L):
    result = []
    for e in L:
        if type(e) != type(L):
            result.append(e)
        else:
            x = flatten(e)
            for i in x:
                result.append(i)
    return result

print(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]))
