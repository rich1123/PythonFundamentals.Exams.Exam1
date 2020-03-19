import typing

def meters_to_feet(meters: float) -> float:
    """
    This function takes a float representing a measurement in meters
    and returns the corresponding value converted to feet.
    The result is rounded to 2 decimal places.

    :param meters: A float representing a measurement in meters.
    :return: A float representing the input measurement converted to feet.
    """
    # feet = (meters * 3.28)
    # return round(feet, 2)
    # meters = float(meters)
    feet = float(meters * 3.28084)
    return float(round(feet, 2))



def feet_to_meters(feet: float) -> float:
    """
    This function takes a float representing a measurement in feet
    and returns the corresponding value converted to meters.
    The result is rounded to 2 decimal places.

    :param feet: A float representing a measurement in feet.
    :return: A float representing the input measurement converted to meters.
    """
    meters = feet * 0.3048000097536
    return round(meters, 2)


def kilometer_to_miles(kilometers: float) -> float:
    """
    This function takes a float representing a measurement in kilometers
    and returns the corresponding value converted to miles.
    The result is rounded to 2 decimal places.

    :param kilometers: A float representing a measurement in kilometers.
    :return: A float representing the input measurement converted to miles.
    """
    miles = kilometers * 0.62137121212121215752
    return round(miles, 2)


def miles_to_kilometers(miles: float) -> float:
    """
    This function takes a float representing a measurement in miles
    and returns the corresponding value converted to kilometers.
    The result is rounded to 2 decimal places.

    :param miles: A float representing a measurement in miles.
    :return: A float representing the input measurement converted to kilometers.
    """
    kilometers = miles * 1.60934
    return round(kilometers, 2)



meters_to_feet(2.0)
feet_to_meters(125.0)
kilometer_to_miles(3.54)
miles_to_kilometers(3.54)
