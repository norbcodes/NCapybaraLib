"""
NCapybaraLib

String submodule for string operations.

https://pypi.org/project/NCapybaraLib/
"""

def insert(string: str, substring: str, index: int) -> str:
    """
    Insert *substring* at index inside *string*.
    If index is higher than the length of the string, the substrings is placed at the end.

    :param string: The original string.
    :param substring: What to insert at the specified index.
    :param index: Where to put substring.
    :return:
    """
    left_half = string[0:index:1]
    right_half = string[index::1]
    return substring.join( (left_half, right_half) )