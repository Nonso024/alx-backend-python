#!/usr/bin/env python3
""" A measuremnt for runtime of concurrent programs """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ fuction that measures time """

    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - s
    return end / n
