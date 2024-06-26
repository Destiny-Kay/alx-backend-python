#!/usr/bin/env python3
'''Python asyncio comprehension'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Collects 10 random numbers using an async
    comprehension over async_generator
    Returns:
        10 random numbers
    '''
    numbers = [i async for i in async_generator()]
    return numbers
