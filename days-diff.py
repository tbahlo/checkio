import datetime


def days_diff(date1, date2):
    first_date = datetime.datetime(year=date1[0], month=date1[1], day=date1[2])
    second_date = datetime.datetime(year=date2[0], month=date2[1], day=date2[2])
    return abs((first_date - second_date).days)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
