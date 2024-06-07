#!/usr/bin/env python3
'''Python Func annotations'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes in a string and an int and returns a tuple'''
    return (k, v**2)
