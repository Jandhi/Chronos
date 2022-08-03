def not_none(*args):
    for arg in args:
        if arg is not None:
            return arg

def min_index(string : str, *substrings):
    min = None

    for substring in substrings:
        if substring in string and (min is None or string.index(substring) < min):
            min = string.index(substring)
    
    return min

DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')