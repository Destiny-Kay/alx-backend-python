#!/usr/bin/env python3
'''Asyncio comprehension'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''
    Runs a couroutine four times in parallel
    '''
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return (time.time() - start)
