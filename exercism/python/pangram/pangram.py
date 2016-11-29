import string


def is_pangram(pangram):
    lower = string.ascii_lowercase
    for c in set(pangram.lower()):
        lower = lower.replace(c, '')
    if not lower:
        return True
    return False
