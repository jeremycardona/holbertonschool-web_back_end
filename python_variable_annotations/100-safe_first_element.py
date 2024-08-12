#!/usr/bin/env python3
"""safe first elements"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """safe first element"""
    if lst:
        return lst[0]
    return None
