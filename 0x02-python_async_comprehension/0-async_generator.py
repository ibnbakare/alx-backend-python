#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    '''sequence of 10 numbers.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
