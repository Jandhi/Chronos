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

def count_combining(string : str):
    count = 0
    for i in range(len(string)):
        if string[i] in COMBINING:
            count += 1
    return count

COMBINING = ('\u0301', '\u0304', '\u0302', '\u0303', '\u0331', '\u2040', '\u0361')