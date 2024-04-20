"""
NCapybaraLib; By NorbCodes.

A small library with a bunch of functions and thingies I made for fun.

https://pypi.org/project/NCapybaraLib/
"""

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