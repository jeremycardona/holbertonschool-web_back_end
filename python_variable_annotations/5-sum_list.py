#!/usr/bin/env python3
""" complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    "sum list of floats and return a float"
    s: float = 0.0
    for f in input_list:
        s += f
    return s
