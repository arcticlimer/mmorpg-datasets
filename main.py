#!/usr/bin/env python3

import asyncio
import os

import aiohttp

import gw2
import hypixel_skyblock


MODULE_LIST = [hypixel_skyblock, gw2]


async def main():
    async with aiohttp.ClientSession() as session:
        coroutines = (module.run(session) for module in MODULE_LIST)
        await asyncio.gather(*coroutines)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    asyncio.run(main())
