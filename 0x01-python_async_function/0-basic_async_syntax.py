#!/usr/bin/env python3
'''Develop
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waiting
    '''
    time = random.random() * max_delay
    await asyncio.sleep(time)
    return time
