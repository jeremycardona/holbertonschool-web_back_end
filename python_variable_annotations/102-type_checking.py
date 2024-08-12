#!/usr/bin/env python3
"""type checking with mypy"""
from typing import Tuple, Generator


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """Zoom array"""
    if not isinstance(factor, int):
        raise TypeError("factor must be an int")

    zoomed_in: Generator[int, None, None] = (
        item for item in lst
        for _ in range(factor)
    )

    return tuple(zoomed_in)


array = (12, 72, 91)


zoom_2x = zoom_array(array)

# Correct the factor to be an integer
zoom_3x = zoom_array(array, 3)
