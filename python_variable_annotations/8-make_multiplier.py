#!/usr/bin/env python3
"""complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a multiplier function"""
    def multiplier_function(value: float) -> float:
        """take a multiplier artgument and return  a float by the multiplier"""
        return value * multiplier
    return multiplier_function
