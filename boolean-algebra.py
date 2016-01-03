OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    #conjunction
    if operation == OPERATION_NAMES[0]:
        return ( x and y )

    #disjunction
    if operation == OPERATION_NAMES[1]:
        return ( x or y )

    #implication
    if operation == OPERATION_NAMES[2]:
        return ( (not x) or y )
    #exclusive
    if operation == OPERATION_NAMES[3]:
        return (x or y) and (not (x and y))

    #equivalence
    if operation == OPERATION_NAMES[4]:
        return not (boolean(x, y, "exclusive"))

    else:
        print("ERROR - operation unknown: ", operation)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
