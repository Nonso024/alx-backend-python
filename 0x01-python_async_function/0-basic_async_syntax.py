#!/usr/bin/env python3
""" An asynchronous funtion """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Takes in an integer, waits for a delay and returns it """

    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
