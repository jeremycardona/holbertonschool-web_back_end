#!/usr/bin/env python3
""" the basics of async """
import asyncio
import random


async def wait_randon(max_delay: int = 10) -> float:
    """function that takes an int and waits for a random delay between 0 and max_delay"""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)

    return wait
