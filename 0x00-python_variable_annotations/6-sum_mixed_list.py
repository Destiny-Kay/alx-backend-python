#!/usr/bin/env python3
'''Func annotations in python'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns the sum of list of elements'''
    return sum(mxd_lst)
