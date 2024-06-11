#!/usr/bin/env python3
'''Python asuncio
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
        Waits for a random number of seconds.
        Args:
            max_delay: the maximum delat time allowable: int
        Returns: returns the wait time
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
