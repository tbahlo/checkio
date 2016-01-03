def checkio(words):
    word_counter = 0
    splitted_text = str(words).split()
    for word in splitted_text:
        if not str(word).isdigit():
            word_counter += 1
            if word_counter >= 3:
                return True
        else:
            word_counter = 0
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
