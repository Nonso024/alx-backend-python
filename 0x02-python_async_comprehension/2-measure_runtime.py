#!/usr/bin/env python3
""" The function measure run time of another sync func """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures runtime of program """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    time_elapsed = time.perf_counter() - start_time
    return time_elapsed
