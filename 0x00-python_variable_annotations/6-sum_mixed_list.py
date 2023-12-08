#!/usr/bin/env python3
""" Type annotated sum_mixed_list function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        This function accepts a list of integers and floats
        Returns the sum as float
    """

    return float(sum(mxd_lst))
