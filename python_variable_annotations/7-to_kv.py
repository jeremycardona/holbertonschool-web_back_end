#!/usr/bin/env python3
"""complex types - string and int/flaot to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """tuple of string and float"""
    square: float = v ** 2
    return (k, square)
