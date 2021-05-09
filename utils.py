import pathlib
import time
import json

import aiofiles


async def write_json(path: str, filename: str, content: str):
    # Create the folders if the path doesn't exist
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    async with aiofiles.open(f'{path}/{filename}.json', mode='w') as f:
        await f.write(content)


def timestamp():
    return round(time.time())
