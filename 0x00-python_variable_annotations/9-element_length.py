#!/usr/bin/env python3
'''Func type annotations'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns length of elements'''
    return [(i, len(i)) for i in lst]
