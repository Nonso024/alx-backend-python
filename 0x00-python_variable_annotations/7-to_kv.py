#!/usr/bin/env python3
"""
    Type-annotated function to_kv which accepts a string k
    and an int||float v and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple """

    return (k, v * v)