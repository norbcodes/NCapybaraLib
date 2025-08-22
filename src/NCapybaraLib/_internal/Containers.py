# MIT License
#
# Copyright (c) 2024 NorbCodes (a.k.a norb3695 or Norb)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
NCapybaraLib; By NorbCodes.

Submodule for working with containers.

https://pypi.org/project/NCapybaraLib/
"""

from math import floor
from typing import Any, Container, TypeVar

n = TypeVar("n")
m = TypeVar("m")

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

def contains(val: Any, check_in: Container[n] | list[Container[n]]) -> bool:
    """
    Checks if `val` is present in the containers.

    :param val: The value.
    :param check_in: Container/Containers.
    :return: Boolean.
    """
    if isinstance(check_in[0], Container):
        for container in check_in:
            if val not in container:
                return False
        return True
    else:
        return val in check_in

def not_contains(val: Any, check_in: Container[n] | list[Container[n]]) -> bool:
    """
    Checks if `val` is NOT present in all provided containers.

    :param val: The value.
    :param check_in: Container/Containers.
    :return: Boolean.
    """
    if isinstance(check_in[0], Container):
        for container in check_in:
            if val in container:
                return False
        return True
    else:
        return val not in check_in

def clean(array: list[n] | tuple[n, ...] | set[n] | dict[n, m]) -> list[n] | tuple[n, ...] | set[n] | dict[n, m] | None:
    """
    Clear out any "" strings from `array`.

    :param array: The array
    :return: The cleaned array.
    """
    if isinstance(array, list):
        new_list = []
        for i in array:
            if i != "":
                new_list.append(i)
        return new_list
    if isinstance(array, tuple):
        new_tuple = []
        for i in array:
            if i != "":
                new_tuple.append(i)
        return tuple(new_tuple)
    if isinstance(array, set):
        new_set = []
        for i in array:
            if i != "":
                new_set.append(i)
        return set(new_set)
    if isinstance(array, dict):
        new_dict = {}
        for i in array:
            if i != "":
                if array[i] != "":
                    new_dict[i] = array[i]
        return new_dict
    return None

# MIT License
#
# Copyright (c) 2024 NorbCodes (a.k.a norb3695 or Norb)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.