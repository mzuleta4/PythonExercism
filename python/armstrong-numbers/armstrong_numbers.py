def is_armstrong_number(number):
    poten = len(str(number))
    return True if sum((int(x) ** poten) for x in str(number)) == number else False

