#!/usr/bin/env python3
""" Type-annotated make_multipler function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a multiplier function """

    return lambda x: x * multiplier
