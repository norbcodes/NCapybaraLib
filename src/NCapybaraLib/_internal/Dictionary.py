"""
NCapybaraLib; By NorbCodes.

Submodule for dictionaries and stuff.

https://pypi.org/project/NCapybaraLib/
"""

from math import floor
from typing import Any

def map_inputs(_first: list[Any], _second: list[Any]) -> dict[Any, Any]:
    """
    Maps items from list *b* to keys from list *a*.

    :param _first: List of keys.
    :param _second: List of items to map to keys.
    :return: A dictionary of the mapped key value pairs.
    """
    if len(_first) == 0 or len(_second) == 0:
        raise ValueError("Either list 'a' or 'b' is empty!")
    # Cannot have more items than keys.
    if len(_second) > len(_first):
        raise Exception("List 'b' cannot be longer than 'a'.")
    # If only one item is provided:
    if len(_second) == 1:
        return {k: _second[0] for k in _first}  # Quick dictionary comprehension :P
    # With that out of the way...
    # Let's get cooking!
    if len(_second) % 2 != 0:
        _second.append(_second[-1])
    if len(_first) % 2 != 0:
        len_a = len(_first) + 1
    else:
        len_a = len(_first)
    NextStepIn = floor(len_a / len(_second))
    Step = 0
    Index = 0
    Temp = {}
    for k in _first:
        if Step == NextStepIn:
            Step = 0
            Index += 1
        Temp[k] = _second[Index]
        Step += 1

    return Temp