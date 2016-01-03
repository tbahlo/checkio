from datetime import date
import datetime


def checkio(from_date, to_date):
    current_day = from_date
    n_free_days = 0
    while current_day <= to_date:
        if current_day.isoweekday() == 6 or current_day.isoweekday() == 7:
            n_free_days += 1
        current_day += datetime.timedelta(days=1)
    return n_free_days

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

