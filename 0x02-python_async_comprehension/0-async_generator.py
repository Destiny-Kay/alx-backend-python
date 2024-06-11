#!/usr/bin/env python3
'''Python asyncio comprehension'''
import random
import asyncio


async def async_generator():
    '''A couroutine that takes no arguments, waits for 1 sec.loops 10 times'''
    i = 0
    while i in range(10):
        await asyncio.sleep(1)
        i += 1
        yield random.random() * 10
