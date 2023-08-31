#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax.
    Write a function (do not create an async function, use the regular function
    syntax to do this) task_wait_random that takes an integer max_delay and
    returns a asyncio.Task. """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Tasks """
    task = asyncio.create_task(wait_random(max_delay))
    return task

    Create a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
    Use the time module to measure an approximate elapsed time.