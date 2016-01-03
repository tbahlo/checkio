def checkio(first, second):
    first_words = str(first).split(sep=",")
    second_words = str(second).split(sep=",")
    common_words = set()
    result_string=""

    for first_iter in first_words:
        for second_iter in second_words:
            if first_iter == second_iter:
                common_words.add(first_iter)
    # trim output:
    common_words = sorted(common_words)
    if common_words != set(): # at least one common word found
        for word in common_words:
            result_string += str(word) + ","
        result_string = result_string[:-1]
    return result_string

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
