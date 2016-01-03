VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import string

def isLong(word):
    if len(word) > 1:
        return True
    else:
        return False

def containsNumbers(word):
    for letter in word:
        if letter in string.digits:
            return True
    return False

def isAlternating(word):
    for letter_iter in range(0, len(word) - 1):
        if (word[letter_iter] in VOWELS) and (word[letter_iter + 1] in VOWELS):
            return False
        if (word[letter_iter] in CONSONANTS) and (word[letter_iter + 1] in CONSONANTS):
            return False
    return True

def checkio(text):
    # replace puntuation with whitespace and switch to uppercase
    for symbol in string.punctuation:
        text = text.replace(symbol, " ")
    text = text.upper()

    # split to single words
    words = text.split()

    # check for counting criteria
    word_counter = 0
    for current_word in words:
        if isLong(current_word) and not containsNumbers(current_word) and isAlternating(current_word):
            word_counter += 1
    return word_counter


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
