def is_leap_year(year: int) -> bool:
    """
    Given a year, this function returns a boolean indicating whether or not it is a leap year.

    :param year: an integer indicating a year.
    :return: A boolean indicating whether or not the year parameter is a leap year.
    """

    # leap = 2000
    if year % 100 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        return True
    if year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return False


is_leap_year(2000)
is_leap_year(1986)
is_leap_year(1971)
is_leap_year(1972)
is_leap_year(-1000)
