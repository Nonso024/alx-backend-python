#!/usr/bin/env python3
""" type-annotated function element_length """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the length of the element """

    return [(i, len(i)) for i in lst]
