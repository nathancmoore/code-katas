"""Kata: To Jaden Case - Capitalize Every Word.

#1 Best Practices Solution by Azuaron et al.

def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())

"""


def to_jaden_case(string):
    """Take in human words and return Jaden Smith Words."""
    list = string.split()
    capitalized_list = []
    for word in list:
        capitalized_list.append(word.capitalize())

    return ' '.join(capitalized_list)
