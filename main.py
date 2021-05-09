#!/usr/bin/env python3

import asyncio
import os

import aiohttp

import gw2
import hypixel_skyblock


COROUTINES = [hypixel_skyblock.run, gw2.run]


async def main():
    async with aiohttp.ClientSession() as session:
        for coro in COROUTINES:
            await asyncio.create_task(coro(session))


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    asyncio.run(main())
