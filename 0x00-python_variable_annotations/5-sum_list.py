#!/usr/bin/env python3
'''Python annotations'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''takes in a input list of floats and returns their sum'''
    return float(sum(input_list))
