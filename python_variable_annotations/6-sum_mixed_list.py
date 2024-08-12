#!/usr/bin/env python3
"""complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of integers and floats returning a float"""
    s: float = 0.0
    for m in mxd_lst:
        s += m
    return s
