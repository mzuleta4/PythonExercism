def is_isogram(string):
    specials = [" ", "-", "."]
    for i in specials:
        string = string.replace(i, "")
    return len(string.lower()) == len(set(string.lower()))