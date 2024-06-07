#!/usr/bin/env python3
'''Func annotations in python'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by multiplier'''
    def func(num: float) -> float:
        '''multiplies a float with multiplier'''
        return num * multiplier
    return func
