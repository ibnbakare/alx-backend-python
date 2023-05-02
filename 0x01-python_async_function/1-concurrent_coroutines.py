#!/usr/bin/python3
"""multiple coroutines
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay)->int:
    """multiple coroutines
    """

    arr = []
    for i in range(n):
        arr.append(await wait_random(max_delay))
    return sorted(arr)
