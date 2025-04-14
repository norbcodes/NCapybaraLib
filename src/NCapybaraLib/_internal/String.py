"""
NCapybaraLib; By NorbCodes.

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
    :return: The final string.
    """
    left_half = string[0:index:1]
    right_half = string[index:None:1]
    return substring.join( (left_half, right_half) )

def _string_similarity_algo(string: str, match: str, case_sensitivity: bool, round_output: int) -> float:
    # yeah
    total_points = 1 + min(len(string), len(match))
    current_points = 0
    # Case sensitivity off?
    if not case_sensitivity:
        string = string.casefold()
        match = match.casefold()

    # If the lengths of BOTH strings are the same
    if len(string) == len(match):
        current_points += 1
    else:
        if len(string) > len(match):
            string = string[0:len(match):1]
        else:
            match = match[0:len(string):1]
    # We know for a fact that both strings are the same length now
    for a, b in zip(string, match):
        if a == b:
            current_points += 1

    if round_output != 0:
        return round(current_points / total_points, round_output)
    else:
        return current_points / total_points

def string_similarity(string: str,
                      match: str | list[str],
                      case_sensitivity: bool = True,
                      round_output: int = 0) -> float | list[float]:
    """
    Uses a very epic cool algorithm to check how similar two strings are.
    The result is a float between 0 and 1, 0 being 0% and 100%.

    :param string: The target string to match against.
    :param match: The string/list of strings to match against the target string.
    :param case_sensitivity: Case sensitivity, default True. If enabled, *Hello* and *hello* will not be
                             a 100% match, but if case sensitivity is disabled, *Hello* and *hello* will produce a 100% match.
    :param round_output: Round the output to a specified decimal point. Default 0 (no rounding).
    :return: A float between 0 and 1, or a list of floats if multiple match strings were passed.
    """
    if isinstance(match, str):
        return _string_similarity_algo(string, match, case_sensitivity, round_output)
    elif isinstance(match, list):
        points: list[float] = []
        for m in match:
            points.append(_string_similarity_algo(string, m, case_sensitivity, round_output))
        return points

def is_palindrome(string: str,
                  also_spaces: bool = False,
                  case_sensitive: bool = False,
                  ignore_non_letters: bool = True) -> bool:
    """
    Checks if a string is a palindrome.

    :param string: The string to check.
    :param also_spaces: Specify whether to check with spaces or not. "a toyota" would return `False` if this option is
                        `True`, however it will return `True` if this option is `False`. This option removes whitespace, tabs and other invisible characters.
    :param case_sensitive: Specify whether the function is case-sensitive.
    :param ignore_non_letters: Specify whether to ignore non-letter characters, such as punctuation.
                               "do geese see god?" would return `False` with this option set to `True`.
                               This option does not exclude numbers.
    :return:
    """
    # Yeaaaah!!!
    # Case sensitive?
    if not case_sensitive:
        string = string.casefold()
    # Also spaces?
    if not also_spaces:
        _temp_string = ""
        for char in string:
            if not char.isspace():
                _temp_string += char
        string = _temp_string
        del _temp_string
    # Ignore non letter chars?
    if ignore_non_letters:
        _temp_string = ""
        for char in string:
            if char.isalnum():
                _temp_string += char
        string = _temp_string
        del _temp_string
    # Finally, check
    return string == string[::-1]