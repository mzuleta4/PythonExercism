import string


def is_pangram(sentence):
    alpha = list(string.ascii_lowercase)
    count = sum(1 for i in alpha if i in sentence.lower())

    return True if count == 26 else False