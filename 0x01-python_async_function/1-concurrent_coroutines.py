#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Runs wait_random n times.
    '''
    arr = []
    for i in range(n):
        arr.append(await wait_random(max_delay))
    return sorted(arr)
