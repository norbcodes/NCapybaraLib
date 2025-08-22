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

Submodule for math stuffs

https://pypi.org/project/NCapybaraLib/
"""

def get_xy_in_2d_array(pos: int, width: int) -> tuple[int, int]:
    """
    Get X,Y coordinates using the index inside a 2D array.

    :param pos: The index.
    :param width: The width of the 2D array.
    :return: The X,Y coords.
    """
    Y = pos // width
    X = pos - (Y * width)
    return X, Y

def get_index_in_2d_array(x: int, y: int, width: int) -> int:
    """
    Get index inside the 2D array using X,Y coordinates.

    :param x: The X position.
    :param y: The Y position.
    :param width: The width of the 2D array.
    :return: The index :)
    """
    return (y * width) + x

def tetration(base: int, exponent: int) -> int:
    """
    Tetration!

    :param base: The base.
    :param exponent: The exponent.
    :return: The result.
    """
    out = base
    for _ in range(exponent-1):
        out = base ** out
    return out

def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
    """
    clamp

    :param value: The value to clamp, duh?!
    :param minimum: If value is below this number, return the later
    :param maximum: If value is above this number, return the later

    and yeah that's literally all
    """
    
    # mf366 here saying "fuck abbreviating shit"
    # "I shall use the correct nerdy terms :nerd:"
    
    if value < minimum:
        return minimum

    if value > maximum:
        return maximum

    return value  # Simply genius code. <3

def range_scale(val: int | float,
                min: int | float,
                max: int | float,
                new_min: int | float,
                new_max: int | float) -> int | float:
    """
    Takes `val`, that is in the range of `min` to `max`, and scales it to be within range of `new_min` to `new_max`.
    Value of 0.5 that is in range 0->1, will turn to 5 when scaled to range 0->10.
    Value of 50 that is in range 0->100, will turn to 5 when scaled to range 0->10.

    :param val: The variable to scale.
    :param min: Minimum allowed value of the variable.
    :param max: Maximum allowed value of the variable.
    :param new_min: Minimum value of the new range.
    :param new_max: Maximum value of the new range.
    :return: The scaled variable.
    """
    normalized = (val - min) / (max - min)
    return (normalized * (new_max - new_min)) + new_min

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