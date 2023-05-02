#!/usr/bin/env python3
'''First task
'''
import asyncio
import random

async def wait_random(max_delay = 10):
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return print(time)

