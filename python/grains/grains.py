def square(number):
    if not valid_number(number):
        raise ValueError("The number isn't between 1 and 64 and should be greater 0")
    return 2**(number - 1)


def valid_number(number):
    return 0 < number < 65


def total():
    return sum(square(x) for x in range(1, 65))
