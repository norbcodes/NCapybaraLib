"""
NCapybaraLib; By NorbCodes.

Submodule for dictionaries and stuff.

https://pypi.org/project/NCapybaraLib/
"""

from math import floor
from typing import Any

def map_inputs(a: list[Any], b: list[Any]) -> dict[Any, Any]:
    """
    Maps items from list *b* to keys from list *a*.

    :param a: List of keys.
    :param b: List of items to map to keys.
    :return: A dictionary of the mapped key value pairs.
    """
    if len(a) == 0 or len(b) == 0:
        raise ValueError("Either list 'a' or 'b' is empty!")
    # Cannot have more items than keys.
    if len(b) > len(a):
        raise Exception("List 'b' cannot be longer than 'a'.")
    # If only one item is provided:
    if len(b) == 1:
        return {k: b[0] for k in a}  # Quick dictionary comprehension :P
    # With that out of the way...
    # Let's get cooking!
    if len(b) % 2 != 0:
        b.append(b[-1])
    if len(a) % 2 != 0:
        len_a = len(a) + 1
    else:
        len_a = len(a)
    NextStepIn = floor(len_a / len(b))
    Step = 0
    Index = 0
    Temp = {}
    for k in a:
        if Step == NextStepIn:
            Step = 0
            Index += 1
        Temp[k] = b[Index]
        Step += 1

    return Temp