def letter_queue(commands):
    stack=""
    for word in commands:
        if str(word).startswith("PUSH"):
            stack += word[5]
        if str(word).startswith("POP"):
            if len(stack) > 0:
                stack = stack[1:]
    return stack

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
