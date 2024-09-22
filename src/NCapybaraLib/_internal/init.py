"""
NCapybaraLib; By NorbCodes.

A small library with a bunch of functions and thingies I made for fun.

https://pypi.org/project/NCapybaraLib/
"""

import os
import sys
from typing import Any, Callable

def print_hello_world() -> None:
    """
    Hello world program straight from NCapybaraLib itself.
    """
    print("Hello world!")

def inject_function(obj: Any, func_name: str, func: Callable[[Any], Any]) -> Any:
    """
    Does exactly what it sounds like. Injects *func* as a method for *obj* under the name *func_name*.

    :param obj: The object instance name referring to the object to inject into.
    :param func_name: The method name.
    :param func: The function to inject.
    :return: The *obj* that was passed in, now with the function injected in it.
    """
    scope = {"target": obj, "injection": func}
    try:
        exec(f"target.{func_name}=classmethod(injection).__get__(None, target)", scope)
    except AttributeError as A:
        raise AttributeError(f"Cannot inject function {func.__name__} as {func_name} into object of type {type(obj)}.") from A
    return scope["target"]

def clear_console() -> None:
    """
    Simple shrimple function to clear the console.
    """
    if sys.platform.casefold() == "win32":
        os.system("cls")
    else:
        os.system("clear")

def nullish_operator(value: Any, new_value: Any) -> Any:
    """
    nullish_operator
    
    Recreation of the GameMaker Studio 2's nullish operator (??) and self nullish operator (=??).

    For more information on how the operator is used in GMS2 visit: https://manual.gamemaker.io/monthly/en/GameMaker_Language/GML_Overview/Expressions_And_Operators.htm?rhhlterm=nullish#

    :param value: The value to return if itself is not None
    :param new_value: The value to return if value is None

    Example usage of the recreation in Python:
    ```
    username = nullish_operator(data.username, "INVALID USERNAME")
    ```
    """
    
    # yet another contribution from y'allsss buddy MF366
    return new_value if value is None else value