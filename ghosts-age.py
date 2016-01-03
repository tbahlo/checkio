MAX_AGE = 5000
fib_numbers = [0, 1]
opacities = {10000: 0}


def calculate_fib_numbers(maximum):
    first = 0
    second = 1
    while second <= maximum:
        dummy = second
        second = first + second
        first = dummy
        fib_numbers.append(second)


def is_fib_number(number):
    if number in fib_numbers:
        return True
    else:
        return False


def calculate_opacities():
    last_opacity = 10000
    for age in range(1, MAX_AGE + 1):
        if is_fib_number(age):
            opacities[last_opacity - age] = age
            last_opacity -= age
        else:
            opacities[last_opacity + 1] = age
            last_opacity += 1


def checkio(opacity):
    calculate_fib_numbers(MAX_AGE)
    calculate_opacities()
    return opacities[opacity]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
