#!/usr/bin/env python3
""" complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    "sum list of floats and return a float"
    s: float = 0.0
    for f in input_list:
        s += f
    return s
