#!/usr/bin/env python3
"""complex types - string and int/flaot to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """tuple of string and float"""
    return (k, float(v ** 2))
