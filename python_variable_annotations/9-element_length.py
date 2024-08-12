#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length"""
    return [(i, len(i)) for i in lst]
