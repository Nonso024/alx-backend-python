#!/usr/bin/env python3
""" Type annotated function returning sum of lists """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Accepts a list of floats and returns sum of all list elements """

    return sum(input_list)
