#!/usr/bin/ env python3
""" Adding typed annotations to a given function """
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ Returns the value of a function safely """

    if key in dct:
        return dct[key]
    else:
        return default
