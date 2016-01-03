def min(*args, **kwargs):
    key = kwargs.get("key", None)

    if key!=None:
        print("found a key function: ", key)
        def keyFunction(arg):
            return key(arg)
    else:
        print("found no key function: ", key)
        def keyFunction(arg):
            return arg

    print("^^ started with args, kwargs:\n", args, "\n", kwargs)
    if len(args)==1:
        print(".. found 1 argument - should be iterable: ", args)
        print("assuming this as first minimum: ", args[0][0])
        minimum=args[0][0]
        for item in args[0]:
            print("test if key(item)<minimum: ", keyFunction(item), "<", keyFunction(minimum))
            if keyFunction(item) < keyFunction(minimum):
                print("new minimum found: ", keyFunction(item))
                minimum = item
        print("returning: ", minimum,"\n###\n")
        return minimum
    else:
        minimum=args[0]
        for item in args:
            if keyFunction(item) < keyFunction(minimum):
                minimum = item
        print("returning: ", minimum,"\n###\n")
        return minimum

def max(*args, **kwargs):
    key = kwargs.get("key", None)

    if key!=None:
        print("found a key function: ", key)
        def keyFunction(arg):
            return key(arg)
    else:
        print("found no key function: ", key)
        def keyFunction(arg):
            return arg

    print("^^ started with args, kwargs:\n", args, "\n", kwargs)
    if len(args)==1:
        print(".. found 1 argument - should be iterable: ", args)
        print("assuming this as first minimum: ", args[0][0])
        maximum=args[0][0]
        for item in args[0]:
            print("test if key(item)>minimum: ", keyFunction(item), ">", keyFunction(maximum))
            if keyFunction(item) > keyFunction(maximum):
                print("new minimum found: ", keyFunction(item))
                maximum = item
        print("returning: ", maximum,"\n###\n")
        return maximum
    else:
        print(".. found several arguments - assuming a list of items")
        maximum=args[0]
        for item in args:
            print("test if key(item)>minimum: ", keyFunction(item), ">", keyFunction(maximum))
            if keyFunction(item) > keyFunction(maximum):
                maximum = item
        print("returning: ", maximum,"\n###\n")
        return maximum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
