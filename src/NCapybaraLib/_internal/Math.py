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
    return base**(base**exponent)  # type: ignore[no-any-return]
    # Yeah what the fuck mypy

def clamp(value: int | float, minimum: int, maximum: int) -> int | float:
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